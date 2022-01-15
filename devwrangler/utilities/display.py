"""CLI and TUI display utilities for devwrangler."""
from rich.console import Console

STD_OUT = Console()
STD_ERR = Console(stderr=True, style="bold red")
