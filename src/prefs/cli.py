# Libraries
import click

# Dependencies
from prefs import bundle, read

@click.group(help="PREFS command line interface tool")
def main():
  pass

@main.command("bundle", help="Bundle a PREFS file into a Python module")
@click.option("--output", default=None, help="The output path")
@click.option("--alias", default=None, help="The alias to be referenced as the path")
@click.argument("path")
def cli_bundle(output, alias, path):
    bundle(path, output, alias)

@main.command("read", help="Reads a PREFS file and displays its content as a Python dictionary")
@click.argument("path")
def cli_read(path):
    click.echo(read(path))
