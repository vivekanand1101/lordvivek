#!/usr/bin/env python
# coding=utf-8

import click

from lordvivek.app import app


@app.command()
def make_someone_give_me_a_rose():
    ''' Like you are getting one '''

    click.echo('Yeah, right. Like you should get one')
