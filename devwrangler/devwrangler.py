"""Main module."""
import json
import platform
import subprocess as sub
import sys
import venv
import warnings
from pathlib import Path
from typing import Any, Callable, Dict, Optional, Sequence

DEFAULT_VSCODE_CONFIG = {
    "editor.formatOnSave": True,
    "files.associations": {
        "**/*.html": "html",
        "**/templates/**/*.html": "django-html",
        "**/templates/**/*": "django-txt",
        "**/requirements{/**,*}.{txt,in}": "pip-requirements",
    },
    "python.analysis.diagnosticPublishDelay": 1000,
    "python.analysis.disabled": [],
    "python.analysis.errors": [
        "inherit-non-class",
        "no-cls-argument",
        "no-self-argument",
        "parameter-already-specified",
        "parameter-missing",
        "positional-argument-after-keyword",
        "positional-only-named",
        "return-in-init",
        "typing-generic-arguments",
        "typing-typevar-arguments",
        "typing-newtype-arguments",
        "unresolved-import",
        "undefined-variable",
    ],
    "python.analysis.warnings": [
        "unknown-parameter-name",
        "variable-not-defined-globally",
        "variable-not-defined-nonlocal",
    ],
    "python.analysis.information": [
        "too-many-function-arguments",
        "too-many-positional-arguments-before-star",
        "no-method-argument",
    ],
    "python.autoComplete.addBrackets": True,
    "python.formatting.provider": "black",
    "python.languageServer": "Pylance",
    "python.linting.banditEnabled": True,
    "python.linting.flake8Enabled": True,
    "python.linting.flake8Args": ["--max-line-length", "88"],
    "python.linting.mypyEnabled": False,
    "python.sortImports.path": "isort",
    "python.sortImports.args": ["--profile", "black"],
    "recommendations": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "hbenl.vscode-test-explorer",
        "littlefoxteam.vscode-python-test-adapter",
        "ms-vscode.test-adapter-converter",
        "samuelcolvin.jinjahtml",
        "batisteo.vscode-django",
        "bungcip.better-toml",
    ],
    "[python]": {
        "editor.insertSpaces": True,
        "editor.tabSize": 4,
        "editor.codeActionsOnSave": {"source.organizeImports": True},
    },
}


def get_py_prefix(venv_path: Path) -> Path:
    """Return the appropriate prefix for the virtual environment's Python.

    >>> # If platform.system() is 'Windows'
    >>> get_py_prefix(Path.cwd()/'.venv')
    Path('.venv/Scripts/python.exe')

    >>> # If platform.system() is not 'Windows'
    >>> get_py_prefix(Path.cwd()/'.venv')
    Path('.venv/bin/python3')
    """
    if platform.system().lower() == 'windows':
        return venv_path / "Scripts" / "python.exe"

    return venv_path / "bin" / "python3"


def create_virtual_environment(venv_path: Path, logger: Callable = print):
    """Generate a virtual environment for the user, including special packages."""
    pretty_path = '/'.join(venv_path.parts[-2:])

    msg = f"Generating virtual environment in {pretty_path}"
    logger(msg)
    try:
        venv.create(
            venv_path,
            with_pip=True,
            prompt=venv_path.parent.name,
            upgrade_deps=True,
        )
    except TypeError:
        # upgrade_deps was introduced in 3.9, without it we need to make a separate
        # call to run_command
        venv.create(venv_path, with_pip=True, prompt=venv_path.parent.name)
        run_command(
            [
                str(get_py_prefix(venv_path)),
                "-m",
                "pip",
                "install",
                "-U",
                "pip",
                "setuptools",
            ]
        )


def install_requirements(
    requirements_path: Path = Path.cwd() / 'requirements.txt',
    venv_path: Path = Path.cwd() / '.venv',
):
    """Install a requirements file, if it exists."""
    run_command(
        [str(get_py_prefix(venv_path)), "pip", "install", "-r", str(requirements_path)]
    )


def parse_config_file(config_file_path: Optional[Path] = None) -> Dict[str, Any]:
    """Parse a devwrangler JSON file.

    >>> parse_config_file(Path.home() / '.devwrangler' / 'config.json')
    { 'vscode': {...}, 'dev_requirements': True, ... }
    """
    if config_file_path is None:
        return DEFAULT_VSCODE_CONFIG
    else:
        with open(config_file_path) as json_file:
            return json.load(json_file)


def set_workspace_settings(config_data: Dict[str, Any], workspace_path: Path):
    """Save the settings.json file for the project."""
    settings_path = workspace_path / 'settings.json'

    if not workspace_path.exists():
        workspace_path.mkdir()

    if not settings_path.exists():
        with open(settings_path, mode='w') as vsc_settings:
            json.dump(config_data, vsc_settings, sort_keys=True, indent=2)
    else:
        with open(settings_path) as f:
            existing_settings = json.load(f)
        config_data |= existing_settings

        with open(settings_path, 'w') as vsc_settings:
            json.dump(config_data, vsc_settings, sort_keys=True, indent=2)


def run_command(command: Sequence[str]):
    """Attempt to run a specific command in the users's shell.

    >>> run_command(['ls'])
    """
    print(f"{' '.join(str(part) for part in command)}")
    try:
        sub.run(
            command,
            check=True,
            encoding="utf-8",
        )
    except sub.CalledProcessError:
        warnings.warn(
            (
                f"Problem encountered when running `{' '.join(command)}`\n\n"
                f"Review the output above to manually debug the issue"
            )
        )
        sys.exit(1)
