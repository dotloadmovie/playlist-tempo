import click as click
from playlist_tempo.app import average_tempo, all_tempos


@click.group()
def tempo():
    """Functions for calculating tempo of playlists"""
    pass


@tempo.command()
@click.option("--playlist", "-p")
def calculate_tempo(playlist):
    print(average_tempo(playlist))


@tempo.command()
@click.option("--playlist", "-p")
def get_all_tempos(playlist):
    print(all_tempos(playlist))
