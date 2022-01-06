"""Test the python -m venv based environment manager."""
import os
from pathlib import Path

import pytest

from devwrangler.managers import VenvManager


def test_venv_creation(tmp_path: Path):
    """Test environment creation with venv."""
    # Arrange
    venv = VenvManager(tmp_path)
    assert not venv.venv_path.exists()
    assert not venv.prefix.exists()

    # Act
    venv.create()

    # Assert
    assert Path(venv.venv_path).exists()
    assert Path(venv.prefix).exists()
    assert os.access(venv.prefix, mode=os.X_OK)


@pytest.mark.skip(reason="Currently unable to install more than minimal dependencies")
def test_dependency_install(tmp_path: Path):
    """Test dependency installation."""
    # Arrange
    tmp_venv = VenvManager(tmp_path)
    tmp_venv.create()

    req_path = tmp_path / "requirements.txt"
    with open(req_path, "w") as req_file:
        req_file.write("cowsay\n")

    cowsay_path = tmp_venv.venv_path.joinpath("bin/cowsay")
    assert not cowsay_path.exists()
    assert tmp_venv.prefix.exists()

    # Act
    assert tmp_venv.prefix.exists()
    tmp_venv.install_dependencies()

    # Assert
    assert cowsay_path.exists()
    assert cowsay_path.is_file()
    assert os.access(cowsay_path, mode=os.X_OK)
