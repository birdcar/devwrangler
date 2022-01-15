"""Typer command module for the Create command."""
from enum import Enum
from pathlib import Path

import typer

from ..managers import CondaManager, VenvManager
from ..utilities.display import STD_OUT

PROJECT_ROOT = Path.cwd()
VENV_PATH = PROJECT_ROOT / ".venv"

create_app = typer.Typer()


class Manager(Enum):
    """An Enum containing the valid managers a user may pick from."""

    conda = "conda"
    venv = "venv"


@create_app.callback()
def main(
    env: Manager = typer.Option(
        'venv',
        metavar="e",
    )
):
    """Create a developer environment."""
    STD_OUT.print(f"[bold green]Creating {env.value} environment...[/]")
    if env == Manager.venv:
        venv = VenvManager()
        venv.create()
        venv.install_dependencies()
    elif env == Manager.conda:
        conda = CondaManager()
        conda.create()
        conda.install_dependencies()


if __name__ == '__main__':
    create_app()
