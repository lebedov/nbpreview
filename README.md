<!-- title-start -->

![nbpreview light logo](https://github.com/paw-lu/nbpreview/blob/main/docs/_static/images/logo_light.svg?raw=True#gh-light-mode-only)
![nbpreview dark logo](https://github.com/paw-lu/nbpreview/blob/main/docs/_static/images/logo_dark.svg?raw=True#gh-dark-mode-only)

# nbpreview

<!-- title-end -->

[![PyPI](https://img.shields.io/pypi/v/nbpreview.svg)](https://pypi.org/project/nbpreview/)
[![Status](https://img.shields.io/pypi/status/nbpreview.svg)](https://pypi.org/project/nbpreview/)
[![Python Version](https://img.shields.io/pypi/pyversions/nbpreview)](https://pypi.org/project/nbpreview)
[![License](https://img.shields.io/pypi/l/nbpreview)](https://opensource.org/licenses/MIT)
[![Read the documentation at https://nbpreview.readthedocs.io/](https://img.shields.io/readthedocs/nbpreview/latest.svg?label=Read%20the%20Docs)][documentation]
[![Tests](https://github.com/paw-lu/nbpreview/workflows/Tests/badge.svg)](https://github.com/paw-lu/nbpreview/actions?workflow=Tests)
[![Codecov](https://codecov.io/gh/paw-lu/nbpreview/branch/main/graph/badge.svg)](https://codecov.io/gh/paw-lu/nbpreview)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![tryceratops](https://img.shields.io/badge/try%2Fexcept%20style-tryceratops%20%F0%9F%A6%96%E2%9C%A8-black)](https://github.com/guilatrova/tryceratops)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

A terminal viewer for Jupyter notebooks.
It's like [cat](https://man7.org/linux/man-pages/man1/cat.1.html)[^cat] for ipynb files.

[^cat]: No, _nbpreview does not actually concatenate files_—but it does print them.

[documentation]: https://nbpreview.readthedocs.io/

<!-- github-only -->

![Hero image](https://github.com/paw-lu/nbpreview/blob/main/docs/_static/images/hero_image.png?raw=True)

## Documentation

nbpreview's [documentation] contains
a detailed breakdown of its [features],
[command-line usage][usage],
and [instructions on how configure][configure] the tool.[^documentation]

## Features

nbpreview can:

- [Syntax highlight code cells](https://nbpreview.readthedocs.io/en/latest/features.html#syntax-highlighting)
- [Render markdown](https://nbpreview.readthedocs.io/en/latest/features.html#markdown-rendering)
- [Draw images](https://nbpreview.readthedocs.io/en/latest/features.html#images)
- [Render DataFrame](https://nbpreview.readthedocs.io/en/latest/features.html#dataframe-rendering)
- [Create previews for Vega charts](https://nbpreview.readthedocs.io/en/latest/features.html#vega-and-vegalite-charts)
- [Render LaTeX](https://nbpreview.readthedocs.io/en/latest/features.html#latex)
- [Parse HTML](https://nbpreview.readthedocs.io/en/latest/features.html#html)
- [Create hyperlinks for complex content](https://nbpreview.readthedocs.io/en/latest/features.html#hyperlinks)
- [Use Nerd Font icons](https://nbpreview.readthedocs.io/en/latest/features.html#nerd-fonts)
- [Render stderr output](https://nbpreview.readthedocs.io/en/latest/features.html#stderr)
- [Render tracebacks](https://nbpreview.readthedocs.io/en/latest/features.html#tracebacks)

## Requirements

- Python 3.8+

## Installation

<!-- installation-start -->

nbpreview can be installed through [pipx] or [pip] from [PyPI](https://pypi.org/).

[pipx] provides an easy way to install Python applications in isolated environments.
[See the documentation for how to install pipx.](https://pypa.github.io/pipx/installation/#install-pipx)

```console
% pipx install nbpreview
```

If [pipx] is not installed,
nbpreview may also be installed via [pip]:

```console
% python -m pip install nbpreview
```

[pipx]: https://pypa.github.io/pipx/
[pip]: https://pip.pypa.io/

<!-- installation-end -->

## Usage

To use nbpreview,
simply type `nbpreview` into your terminal followed by the path of the notebook you wish to view.

```console
% nbpreview notebook.ipynb
```

See the [command-line reference][usage] for details on options.

## Contributing

Contributions are very welcome.
To learn more, see the [contributor guide][contributing].

## License

Distributed under the terms of the [MIT license][license],
_nbpreview_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue][issues] along with a detailed description.

## Prior art

### Similar tools

<!-- similar-tools-start -->

Thanks to [@joouha] for [maintaining list of these tools][euporie_similar_tools].
Many of the projects here were found directly on their page.

- [ipynb-term](https://github.com/PaulEcoffet/ipynbviewer)
- [ipynbat](https://github.com/edgarogh/ipynbat)
- [ipynbviewer](https://github.com/edgarogh/ipynbat)
- [jcat](https://github.com/ktw361/jcat)
- [jupview](https://github.com/Artiomio/jupview)
- [jupytui](https://github.com/mosiman/jupytui)
- [jut](https://github.com/kracekumar/jut)
- [nbcat](https://github.com/jlumpe/nbcat)
- [nbtui](https://github.com/chentau/nbtui)
- [nbv](https://github.com/lepisma/nbv)
- [Read-Jupyter-Notebook](https://github.com/qcw171717/Read-Jupyter-Notebook)

[@joouha]: https://github.com
[euporie_similar_tools]: https://euporie.readthedocs.io/en/latest/pages/related.html#notebook-viewers

<!-- similar-tools-end -->

### Complimentary tools

<!-- complimentary-tools-start -->

If you're interested in complimentary tools
that help improve the terminal experience for notebooks,
there are many amazing projects out there.

- **[bat](https://github.com/sharkdp/bat)**
  is not a tool for notebooks specifically.
  But similar to nbpreview,
  it provides a rich output for many types of files on the terminal,
  and is the primary inspiration for nbpreview.
- **[euporie]**
  is a really exciting project
  that allows you to edit and run Jupyter notebooks on the terminal.
- **[nbclient]**
  is a library for executing notebooks from the command line.
- **[nbqa]**
  allows the use of linters and formatters on notebooks.
  It's also used by this project.
- **[jpterm]**
  is and up-and-coming successor to [nbterm]
  which will be accompanied by a web client.
  Looking forward to seeing this develop.
- **[nbtermix]**
  is an actively-developed fork of [nbterm].
- **[nbterm]**
  lets you edit and execute Jupyter Notebooks on the terminal.
- **[papermill]**
  allows the parameterization and execution of Jupyter Notebooks.

[nbterm]: https://github.com/davidbrochart/nbterm
[euporie]: https://github.com/joouha/euporie
[nbclient]: https://github.com/jupyter/nbclient
[nbqa]: https://github.com/nbQA-dev/nbQA
[jpterm]: https://github.com/davidbrochart/jpterm
[nbtermix]: https://github.com/mtatton/nbtermix
[nbterm]: https://github.com/davidbrochart/nbterm
[papermill]: https://github.com/nteract/papermill

<!-- complimentary-tools-end -->

## Credits

<!-- credits-start -->

nbpreview relies on a lot of fantastic projects.
Check out the [dependencies] for a complete list of libraries that are leveraged.

Besides the direct dependencies,
there are some other projects that directly enabled the development of nbpreview.

- **[bat]**
  is not explicitly used in this project,
  but served as the primary inspiration.
  This projects strives to be [bat]—but
  for notebooks.
  Many of nbpreview's features and command-line options are directly adopted from [bat].
- **[Hypermodern Python Cookiecutter]**
  is the template this project was generated on.
  It is a fantastic template that integrates [Poetry],
  [Nox],
  and [pre-commit].
  It's responsible for most of the underlying structure of this project's CI.
- **[justcharts]**
  is used in this project
  to generate the Vega and Vega-Lite charts.

[bat]: https://github.com/sharkdp/bat
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[justcharts]: https://github.com/koaning/justcharts
[nox]: https://nox.thea.codes/en/stable/
[poetry]: https://python-poetry.org/
[pre-commit]: https://pre-commit.com/

<!-- credits-end -->

[^documentation]: Thanks to [Furo], [MyST], and [Rich][exporting_rich_console].

[configure]: https://nbpreview.readthedocs.io/configure.html
[contributing]: https://github.com/paw-lu/nbpreview/blob/main/CONTRIBUTING.md
[dependencies]: https://github.com/paw-lu/nbpreview/blob/main/pyproject.toml
[exporting_rich_console]: https://rich.readthedocs.io/en/stable/console.html#exporting
[features]: https://nbpreview.readthedocs.io/features.html
[furo]: https://pradyunsg.me/furo/quickstart/
[issues]: https://github.com/paw-lu/nbpreview/issues
[license]: https://opensource.org/licenses/MIT
[myst]: https://myst-parser.readthedocs.io/en/latest/
[usage]: https://nbpreview.readthedocs.io/en/latest/usage.html
