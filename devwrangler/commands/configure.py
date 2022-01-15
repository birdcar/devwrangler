"""Typer command module for the `configure` command."""
from enum import Enum

import typer

from ..utilities.display import STD_OUT

config_app = typer.Typer()


class Editor(Enum):
    """Enum of valid editor options."""

    vscode = "vscode"


def parse_extras(extras: str) -> tuple:
    """Parse a comma separated options list provided by the user."""
    return tuple(s.strip() for s in extras.split(','))


@config_app.callback('configure')
def configure(
    editor: Editor = typer.Option(
        'vscode',
        metavar="e",
        help="The editor you'd like configured for development",
    ),
    extras: str = typer.Option(
        "black,bandit,flake8,jinja2,mypy,isort",
        metavar="x",
        help="Extras to enable and configure in your editor (see docs for supported options)",
        callback=parse_extras,
    ),
):
    """Configure an editor to use an already configured dev environment."""
    STD_OUT.print("Configuring VS Code...")
    STD_OUT.print(f"Configuring extras {extras} in {editor.value}")


if __name__ == '__main__':
    config_app()
