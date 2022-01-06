"""A wrapper for creating a venv-based dev environment."""
import venv

from .base import BaseManager


class VenvManager(BaseManager):
    """Manage virtual environments with Python's 'venv' module."""

    def create(self):
        """Create a virtual environment using venv."""
        venv.create(
            self.venv_path,
            with_pip=True,
            prompt=self.venv_path.parent.name,
        )

    def install_dependencies(self, verbose: bool = False):
        """Install environment dependencies."""
        PIP_CMD = [
            str(self.prefix),
            "-m",
            "pip",
            "install",
            "-U",
            "pip",
            "setuptools",
        ]

        if not verbose:
            PIP_CMD.append("-qqq")

        self.cmd(PIP_CMD)
