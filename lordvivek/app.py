#!/usr/bin/env python

import click
import tempfile


@click.group()
def app():
    pass

__all__ = [
    'app',
]

from lordvivek.rose import make_someone_give_me_a_rose

if  __name__ == '__main__':
    app()
