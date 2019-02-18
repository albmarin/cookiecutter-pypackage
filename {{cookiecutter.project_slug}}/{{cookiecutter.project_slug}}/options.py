# -*- coding: utf-8 -*-

import logging
import platform
import sys

import click

from . import __version__


def get_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    message = (
        f"Python v{platform.python_version()}\n"
        f"{{cookiecutter.project_name}} v{__version__}"
    )
    click.echo(message, color=ctx.color)
    ctx.exit()


def set_log_level(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    level = getattr(logging, value)
    logging.basicConfig(
        stream=sys.stdout,
        format="%(asctime)s|%(levelname)s|%(filename)s:%(lineno)s|%(message)s",
        level=level,
    )


version_option = click.Option(
    ['--version'],
    help='Show the flask version',
    expose_value=False,
    callback=get_version,
    is_flag=True,
    is_eager=True
)

log_option = click.Option(
    ["--log"],
    callback=set_log_level,
    default="INFO",
    help="Set the logging level",
    type=click.Choice(["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"]),
)
