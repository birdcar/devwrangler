import subprocess as sub
import sys
import warnings
from typing import Sequence


def run_command(command: Sequence[str]):
    """Attempt to run a specific command in the users's shell.

    >>> run_command(['ls'])
    """
    try:
        sub.run(
            command,
            check=True,
            encoding="utf-8",
        )
    except sub.CalledProcessError:
        warnings.warn(
            (
                f"Problem encountered when running `{' '.join(command)}`\n\n"
                f"Review the output above to manually debug the issue"
            )
        )
        sys.exit(1)
