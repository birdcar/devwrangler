"""Implement a venv specific manager for those who prefer to use venv."""
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
        minimal_dependencies = [
            str(self.prefix),
            "-m",
            "pip",
            "install",
            "-U",
            "pip",
            "setuptools",
        ]

        if quiet:
            minimal_dependencies.append("-qqq")
        self.cmd(minimal_dependencies)
