"""Tests for the devwrangler.managers.conda module."""

import os
import shutil
from pathlib import Path

import pytest

from devwrangler.managers import CondaManager

if not shutil.which('conda'):
    pytest.skip("skipping conda-only tests", allow_module_level=True)


def test_conda_blank_env_create(tmp_path: Path):
    """Test Conda environment creation in empty folder."""
    # Arrange
    env = CondaManager(tmp_path)
    assert not env.venv_path.exists()
    assert not env.prefix.exists()

    # Act
    env.create()

    # Assert
    assert Path(env.venv_path).exists()
    assert Path(env.prefix).exists()
    assert os.access(env.prefix, mode=os.X_OK)
