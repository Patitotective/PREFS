import os
import click
from prefs import bundle, read

@click.group(help="PREFS command line interface tool")
def main():
  pass

@main.command("bundle", help="Bundle a PREFS file into a Python module")
@click.option("-o", "--output", default=None, help="The output path")
@click.option("-a", "--alias", default=None, help="The alias to be referenced as the path")
@click.argument("path")
def cli_bundle(output, alias, path):
    bundle(path, output, alias)

@main.command("read", help="Reads a PREFS file and displays its content as a Python dictionary")
@click.argument("path")
def cli_read(path):
    path = os.path.join(os.getcwd(), path)
    click.echo(read(path))

@main.command("about", help="Shows information about PREFS")
def cli_about():
    # Ignore that weird multi-line string
    click.echo(
"""
PREFS is a Python library to store and manage preferences.
- Website: https://patitotective.github.io/PREFS.
- Documentation: https://patitotective.github.io/PREFS/docs.
- GitHub: https://github.com/Patitotective/PREFS.
- PyPi: https://pypi.org/project/PREFS/.
Contact me:
- Discord: Patitotective#0127
- Twitter: https://twitter.com/patitotective
- Email: cristobalriaga@gmail.com
""".strip()
    )
