"""Typer-based CLI for devwrangler."""
from pathlib import Path

import typer

from .devwrangler import (
    create_virtual_environment,
    parse_config_file,
    set_workspace_settings,
)

APP_NAME = 'devwrangler'

PROJECT_ROOT = Path.cwd()
VENV_PATH = PROJECT_ROOT / ".venv"


def main(
    req_file: str = typer.Argument('requirements-dev.txt'),
    dev: bool = typer.Argument(True),
):
    """CLI main function."""
    app_dir = typer.get_app_dir(APP_NAME, force_posix=True)
    config_file_path: Path = Path(app_dir) / 'config.json'

    # check if config data exists, if not, proceed with default config
    if not config_file_path.exists():
        typer.echo(f"Config file not found at {config_file_path}")
        typer.echo("Using our default configuration")
        config_data = parse_config_file()
    else:
        config_data = parse_config_file(config_file_path)

    create_virtual_environment(VENV_PATH, logger=typer.echo)
    set_workspace_settings(config_data, workspace_path=(PROJECT_ROOT / '.vscode'))


if __name__ == '__main__':
    main()
