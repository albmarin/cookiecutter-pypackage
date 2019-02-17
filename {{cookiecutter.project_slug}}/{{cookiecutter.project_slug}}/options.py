import platform

import click

from {{cookiecutter.project_slug}} import __version__


def get_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    message = (
        f'Python {platform.python_version()}\n'
        f'{{cookiecutter.project_slug}} {__version__}'
    )
    click.echo(message, color=ctx.color)
    ctx.exit()
