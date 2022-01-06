"""Defines an Abstract Base Class (ABC) to Standardize the API for various environment managers."""
import abc
import platform
from pathlib import Path

from ..utilities.shell import run_command


class BaseManager(abc.ABC):
    """A standard API for various environment managers."""

    def __init__(self, work_dir: Path):
        """Initialize a virtual environment model with venv."""
        self.prefixes = {
            'windows': 'Scripts/python.exe',
        }
        self.venv_path = work_dir / ".venv"
        self.cmd = run_command

    @property
    def prefix(self) -> Path:
        """Return the path to the python executable for the virtual environment."""
        return self.venv_path.joinpath(
            self.prefixes.get(platform.system().lower(), "bin/python")
        )

    @abc.abstractmethod
    def create(self):
        """Create a sandboxed virtual environment with the specific manager."""
        pass

    @abc.abstractmethod
    def install_dependencies(self, verbose: bool = False):
        """Install dependencies into a created environment."""
        pass
