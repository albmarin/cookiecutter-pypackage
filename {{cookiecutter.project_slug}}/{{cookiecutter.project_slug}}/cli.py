# -*- coding: utf-8 -*-

"""Console script for {{cookiecutter.project_slug}}."""
import logging
import sys

import click

from .options import get_version


@click.command()
@click.option(
    "--log",
    default="INFO",
    help="Set the logging level",
    type=click.Choice(["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"]),
)
@click.option(
    '--version',
    help='Show the App version',
    expose_value=False,
    callback=get_version,
    is_flag=True,
    is_eager=True
)
def main(log, args=None):
    """Console script for {{cookiecutter.project_slug}}."""
    level = getattr(logging, log)
    logging.basicConfig(
        stream=sys.stdout,
        format="%(asctime)s|%(levelname)s|%(filename)s:%(lineno)s|%(message)s",
        level=level,
    )

    click.echo("Replace this message by putting your code into "
               "{{cookiecutter.project_slug}}.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
