import click


@click.command()
@click.option('-pkf', '--privateKeyFile', type=str, help="Set private key file path",
              prompt="Enter path to private key file")
@click.option('-gkj', '--generatedKeyJson', type=str, help="Set name of generated key.json",
              prompt="Enter name of generating key json file")
def create_keystore(privateKeyFile, generatedKeyJson):
    click.echo(f"{privateKeyFile, generatedKeyJson}")
