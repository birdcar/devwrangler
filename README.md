# Dev Wrangler

[![pypi](https://img.shields.io/pypi/v/devwrangler.svg)](https://pypi.org/project/devwrangler/)
[![python](https://img.shields.io/pypi/pyversions/devwrangler.svg)](https://pypi.org/project/devwrangler/)
[![Build Status](https://github.com/birdcar/devwrangler/actions/workflows/dev.yml/badge.svg)](https://github.com/birdcar/devwrangler/actions/workflows/dev.yml)
[![codecov](https://codecov.io/gh/birdcar/devwrangler/branch/main/graphs/badge.svg)](https://codecov.io/github/birdcar/devwrangler)

Bringing peace, freedom, justice, and security to your Python empire

* Documentation: <https://birdcar.github.io/devwrangler>
* GitHub: <https://github.com/birdcar/devwrangler>
* PyPI: <https://pypi.org/project/devwrangler/>
* Free software: MIT

## Features

* Single command configuration of:
  * your Python project's virtual environment
  * your project's VS Code settings

## Basic Usage

```shell
$ pydev
$ pydev create
$ pydev create --env venv
$ pydev create --env conda
$ pyenv configure
$ pydev configure --editor vscode
$ pydev configure --editor vscode --extras django,jinja2
```


## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage) project template.
