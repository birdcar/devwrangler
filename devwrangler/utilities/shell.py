"""Shell command uitilities for devwrangler."""
import subprocess as sub
import sys
from typing import Sequence

from .logging import LOG


def run_command(command: str | Sequence[str], critical: bool = False, **kwargs):
    """Attempt to run a specific command in the users's shell.

    >>> run_command('ls')
    """
    try:
        command_process = sub.run(
            command,
            shell=True,
            check=True,
            encoding="utf-8",
            capture_output=True,
            **kwargs,
        )
        LOG.critical("Are we getting here?")
        LOG.debug(command_process.stdout)
    except sub.CalledProcessError as err:
        LOG.error(
            (
                f"Problem encountered when running "
                f"`{' '.join(command) if type(command)=='list' else command}`"
            )
        )
        LOG.error(err.output)

        if critical:
            LOG.critical("Required command failed, exiting with status code 1")
            sys.exit(1)
