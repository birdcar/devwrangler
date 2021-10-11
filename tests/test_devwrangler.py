#!/usr/bin/env python
"""Tests for `devwrangler` package."""
import os
from pathlib import Path

from devwrangler.devwrangler import create_virtual_environment


def test_create_virtualenv(tmpdir):
    """Test that create_virtualenv creates a .venv directory."""
    # Setup
    test_dir = tmpdir.mkdir('venv_test')
    venv_dir = Path(test_dir.join('.venv'))
    os.chdir(test_dir)
    assert not venv_dir.exists()
    assert Path(test_dir) == venv_dir.parent
    create_virtual_environment(venv_dir)
    assert venv_dir.exists()
