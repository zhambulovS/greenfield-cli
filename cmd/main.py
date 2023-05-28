import click
from cmd_config import config
from cmd_keystore import create_keystore

@click.group()
def gnfd():
    pass


gnfd.add_command(config)
gnfd.add_command(create_keystore)
