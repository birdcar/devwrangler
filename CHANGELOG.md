# Changelog

## [0.2.2] - 2021-11-3

### Fixed

* The `settings.json` file that was output by `pydev` was malformed, and this patch ensures that's no longer the case.

## [0.2.1] - 2021-10-10

### Added

* Very basic information has been added to the README file, reflecting the current features of the project.

### Changed

* The virtual environment prompt was being set to the Path to the parent folder, rather than the name of the parent folder itself. This has now been fixed.

## [0.2.0] - 2021-10-10

### Added

* It lives! `pydev` will now work in a *very* alpha form after `devwrangler` is installed with pipx
* One whole test to verify that creating the virtual env works as expected on all supported versions of Python.
* Typer, to manage our CLI niceties rather than writing them from scratch
* Rich, to eventually make the CLI output pretty

## [0.1.1] - 2021-10-07

### Added

* Added support for Python 3.10
* Added dev environment niceties
  * Enabled tighter VS Code integration
  * Specified supported pyenv versions

### Removed

* Dropped support for Python 3.6

## [0.1.0] - 2021-10-07

* First release on PyPI.
