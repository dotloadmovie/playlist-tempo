import click as click
from playlist_tempo.app import average_tempo


@click.group()
def tempo():
    """Functions for calculating tempo of playlists"""
    pass


@tempo.command()
@click.option("--playlist", "-p")
def calculate_tempo(playlist):
    print(average_tempo(playlist))
