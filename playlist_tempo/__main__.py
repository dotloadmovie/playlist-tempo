import click as click

from playlist_tempo.cli import tempo


@click.group()
def cli():
    pass


cli.add_command(tempo)

if __name__ == "__main__":
    cli()
