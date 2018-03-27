# -*- coding: utf-8 -*-

import os

import click

from usage import fetch_usage_json, format_usage_message


@click.command()
def main():
    username = os.environ.get('COX_USERNAME')
    password = os.environ.get('COX_PASSWORD')

    click.echo(format_usage_message(fetch_usage_json(username, password)))
