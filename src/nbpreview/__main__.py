"""Command-line interface."""
import os
import pathlib
from pathlib import Path
from sys import stdin, stdout
from typing import IO, AnyStr, Iterator, List, Literal, Optional, Sequence, Union

import click
import nbformat
import typer
from rich import box, console, panel, style, text, traceback
from rich.console import Capture, Console, RenderableType
from rich.text import Text

from nbpreview import errors, notebook, parameters
from nbpreview.component.content.output.result import drawing
from nbpreview.component.content.output.result.drawing import ImageDrawingEnum
from nbpreview.notebook import Notebook
from nbpreview.parameters import ColorSystemEnum

app = typer.Typer()
traceback.install(theme="material")


def _envvar_to_bool(envvar: str) -> bool:
    """Convert environmental variable values to bool."""
    envvar_value = os.environ.get(envvar, False)
    envvar_bool = bool(envvar_value) and (envvar != "0") and (envvar.lower() != "false")
    return envvar_bool


def _detect_no_color() -> Union[bool, None]:
    """Detect if color should be used."""
    no_color_variables = (
        _envvar_to_bool("NO_COLOR"),
        _envvar_to_bool("NBPREVIEW_NO_COLOR"),
        os.environ.get("TERM", "smart").lower() == "dumb",
    )
    force_no_color = any(no_color_variables)
    return force_no_color


def _check_image_drawing_option(image_drawing: Union[ImageDrawingEnum, None]) -> None:
    """Check if the image drawing option is valid."""
    if image_drawing == drawing.ImageDrawingEnum.BLOCK:
        try:
            import terminedia  # noqa: F401
        except ModuleNotFoundError as exception:
            message = (
                f"--image-drawing='{image_drawing.value}' cannot be"
                " used on this system. This might be because it is"
                " being run on Windows."
            )
            raise typer.BadParameter(
                message=message, param_hint="image-drawing"
            ) from exception


def _detect_paging(
    paging: Union[bool, None], rendered_notebook: str, console: Console
) -> bool:
    """Determine if pager should be used."""
    detected_paging = paging or (
        paging is None
        and console.height < (rendered_notebook.count("\n") + 1)
        and console.is_interactive
        # click.echo_via_pager will not use a pager when stdin or stdout
        # is not a tty, which will result in uncolored output
        # Disable paging for now as a workaround
        # This means a pager will not be used when output is piped
        and stdin.isatty()  # Importing stdin/stdout directly because
        # of trouble in mocking when importing top level sys
        and stdout.isatty()
    )
    return detected_paging


def _render_notebook(
    capture: Capture,
    console: Console,
    paging: Union[bool, None],
    color: Union[bool, None],
) -> None:
    """Render the notebook to the console."""
    rendered_notebook = capture.get()
    _paging = _detect_paging(
        paging, rendered_notebook=rendered_notebook, console=console
    )
    if _paging:
        click.echo_via_pager(rendered_notebook, color=color)
    else:
        print(rendered_notebook, end="")


def _make_invalid_notebook_message(
    file: Union[
        Sequence[Union[Path, IO[AnyStr]]],
        Union[Path, IO[AnyStr]],
    ]
) -> str:
    """Create message signifying which paths are invalid."""
    files = file if isinstance(file, Sequence) else [file]
    file_names = [
        os.fsdecode(file) if isinstance(file, Path) else file.name for file in files
    ]

    if len(file_names) == 1:
        verb = "is"
        plural = ""

    else:
        verb = "are"
        plural = "s"

    invalid_notebook_message = (
        f"{', '.join(file_names)} {verb}" f" not a valid Jupyter Notebook path{plural}."
    )
    return invalid_notebook_message


def _create_file_title(path: Path, width: int) -> str:
    """Create the title for a file panel."""
    title = (
        os.fsdecode(path.name)
        if width < len(path_string := os.fsdecode(path))
        else path_string
    )
    return title


@console.group()
def _title_output(
    renderable: RenderableType,
    plain: bool,
    path: Path,
    has_multiple_files: bool,
    width: int,
) -> Iterator[RenderableType]:
    """If needed, title the output with the file path."""
    if not plain and has_multiple_files:
        border_characters = 6  # 4 for box edges and 2 for padding
        title_width = width - border_characters
        title = _create_file_title(path, width=title_width)
        wrapped_output = panel.Panel(
            renderable,
            box=box.HEAVY,
            title_align="left",
            expand=True,
            padding=(1, 2, 1, 2),
            safe_box=True,
            width=width,
            title=title,
        )
        yield wrapped_output

    else:
        if has_multiple_files and plain:
            title = _create_file_title(path, width=width)
            yield title
            yield text.Text()
        yield renderable

    if has_multiple_files:
        yield text.Text()
        if plain:
            yield text.Text()


@app.command()
def main(
    file: List[Path] = parameters.file_argument,
    theme: Optional[str] = parameters.theme_option,
    list_themes: Optional[bool] = parameters.list_themes_option,
    plain: Optional[bool] = parameters.plain_option,
    unicode: Optional[bool] = parameters.unicode_option,
    hide_output: bool = parameters.hide_output_option,
    nerd_font: bool = parameters.nerd_font_option,
    no_files: bool = parameters.no_files_option,
    positive_space: bool = parameters.positive_space_option,
    hyperlinks: bool = parameters.hyperlinks_option,
    hide_hyperlink_hints: bool = parameters.hide_hyperlink_hints_option,
    images: Optional[bool] = parameters.images_option,
    image_drawing: Optional[ImageDrawingEnum] = parameters.image_drawing_option,
    color: Optional[bool] = parameters.color_option,
    color_system: Optional[ColorSystemEnum] = parameters.color_system_option,
    width: Optional[int] = parameters.width_option,
    version: Optional[bool] = parameters.version_option,
    line_numbers: bool = parameters.line_numbers_option,
    code_wrap: bool = parameters.code_wrap_option,
    paging: Optional[bool] = parameters.paging_option,
) -> None:
    """Render a Jupyter Notebook in the terminal."""
    if color is None and _detect_no_color():
        color = False
    no_color = not color if color is not None else color
    _color_system: Union[
        Literal["auto", "standard", "256", "truecolor", "windows"], None
    ]
    if color_system is None:
        _color_system = "auto"
    elif color_system == "none":
        _color_system = None
    else:
        _color_system = color_system.value

    output_console = console.Console(
        width=width,
        no_color=no_color,
        emoji=unicode if unicode is not None else True,
        color_system=_color_system,
    )

    _check_image_drawing_option(image_drawing)
    files = not no_files
    negative_space = not positive_space
    translated_theme = parameters.translate_theme(theme)

    has_multiple_files = 1 < len(file)
    successful_render = False
    plain_title = notebook.pick_option(plain, detector=not output_console.is_terminal)
    with output_console.capture() as captured_output:
        for notebook_file in file:
            with click.open_file(os.fsdecode(notebook_file)) as opened_notebook_file:
                rendered_file: Union[Notebook, Text]
                try:
                    rendered_file = notebook.Notebook.from_file(
                        opened_notebook_file,
                        theme=translated_theme,
                        hide_output=hide_output,
                        plain=plain,
                        unicode=unicode,
                        nerd_font=nerd_font,
                        files=files,
                        negative_space=negative_space,
                        hyperlinks=hyperlinks,
                        hide_hyperlink_hints=hide_hyperlink_hints,
                        images=images,
                        image_drawing=image_drawing,
                        color=color,
                        line_numbers=line_numbers,
                        code_wrap=code_wrap,
                    )

                except (
                    nbformat.reader.NotJSONError,
                    errors.InvalidNotebookError,
                ):
                    message = _make_invalid_notebook_message(opened_notebook_file)
                    rendered_file = text.Text(
                        message, style=style.Style(color="color(178)")
                    )
                    pass

                else:
                    successful_render = True

                finally:
                    path = pathlib.Path(opened_notebook_file.name)
                    console_width = output_console.width
                    titled_output = _title_output(
                        rendered_file,
                        path=path,
                        width=console_width,
                        plain=plain_title,
                        has_multiple_files=has_multiple_files,
                    )
                    output_console.print(titled_output)

    if successful_render:
        _render_notebook(
            captured_output, console=output_console, paging=paging, color=color
        )

    else:
        message = _make_invalid_notebook_message(file)
        raise typer.BadParameter(message, param_hint="FILE")


typer_click_object = typer.main.get_command(app)
if __name__ == "__main__":
    typer_click_object()  # pragma: no cover
