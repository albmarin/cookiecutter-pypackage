#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    if '{{ cookiecutter.use_pytest }}' == 'y':
        remove_file('tests/__init__.py')

    if '{{ cookiecutter.use_pre_commit_hooks }}' != 'y':
        remove_file('.pre-commit-config.yaml')

    if '{{ cookiecutter.add_pyup_badge }}' != 'y':
        remove_file('.pyup.yml')

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        cli_file = os.path.join('{{ cookiecutter.project_slug }}', 'cli.py')
        main_file = os.path.join('{{ cookiecutter.project_slug }}', '__main__.py')
        options_file = os.path.join('{{ cookiecutter.project_slug }}', 'options.py')

        remove_file(cli_file)
        remove_file(main_file)
        remove_file(options_file)

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')
