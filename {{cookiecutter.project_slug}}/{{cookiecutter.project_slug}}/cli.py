# -*- coding: utf-8 -*-

"""Console script for {{cookiecutter.project_slug}}."""
import logging
import sys

import click
from pcuf.ext.click import add_commands

from .options import version_option, log_option

logger = logging.getLogger(__name__)


class AppGroup(click.Group):
    def __init__(self, **extra):
        params = list(extra.pop("params", None) or ())
        params.append(version_option)
        params.append(log_option)

        click.Group.__init__(self, params=params, **extra)

        # Add Commands
        add_commands(self, (run_command,))


@click.command("run", short_help="Run main function")
def run_command():
    click.echo("Replace this message by putting your code into "
               "{{cookiecutter.project_slug}}.cli.run_command")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


cli = AppGroup(help="""\
Console script for {{cookiecutter.project_name}}.
""")


def main(as_module=False):
    args = sys.argv[1:]

    if as_module:
        this_module = "{{cookiecutter.project_slug}}"
        name = "python -m " + this_module

        # Python rewrites "python -m {{cookiecutter.project_slug}}" to the path to the file in argv.
        # Restore the original command so that the reloader works.
        sys.argv = ["-m", this_module] + args
    else:
        name = None

    cli.main(args=args, prog_name=name)


if __name__ == "__main__":
    sys.exit(main(as_module=True))  # pragma: no cover
