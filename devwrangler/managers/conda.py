"""A wrapper for creating an Anaconda-based dev environment."""
import shutil as sh
from pathlib import Path

from .base import BaseManager


class CondaManager(BaseManager):
    """A manager for conda and it's environment."""

    def create(self):
        """Create a conda environment in the location specified by venv_path."""
        if not sh.which("conda"):
            raise FileNotFoundError("No conda executable found in your $PATH")

        self.cmd(
            [
                "conda",
                "create",
                "-y",
                "--quiet",
                "--prefix",
                str(self.venv_path),
                "python",
            ]
        )

    def install_dependencies(self, verbose: bool = False):
        """Install dependencies from conda's environment.yml file in the root of your project."""
        if not sh.which("conda"):
            raise FileNotFoundError("No conda executable found in your $PATH")

        if not (Path.cwd() / "environment.yml").exists():
            raise FileNotFoundError(
                "No environment.yml file round in the project directory"
            )

        CONDA_CMD = [
            "conda",
            "env",
            "update",
            "--prefix",
            str(self.venv_path),
            "--file",
            "environment.yml",
            "--prune",
        ]

        if not verbose:
            CONDA_CMD.append("--quiet")

        self.cmd(CONDA_CMD)
