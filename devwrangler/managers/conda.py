import shutil as sh

from .base import BaseManager


class CondaManager(BaseManager):
    """A manager for conda and it's environment."""

    def create(self):
        """Create a conda environment in the location specified by venv_path."""
        if not sh.which("conda"):
            raise FileNotFoundError("No conda executable found in your $PATH")

        self.cmd(["conda", "env", "create", "-p", str(self.venv_path)])

    def install_dependencies(self, quiet: bool = True):
        """Install dependencies from conda's environment.yml file in the root of your project."""
        if not sh.which("conda"):
            raise FileNotFoundError("No conda executable found in your $PATH")
        self.cmd(
            [
                "conda",
                "env",
                "update",
                "--prefix",
                str(self.venv_path.parent),
                "--file" "environment.yml",
                "--prune",
            ]
        )
