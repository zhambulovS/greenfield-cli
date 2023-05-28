import click


@click.group('bank')
def bank():
    pass


@click.command('balance')
@click.option('--address', type=str, help="indicate the address's balance to be retrieved",
              prompt="Enter the address's balance to be retrieved")
def balance(address):
    click.echo(f"{address}")


@click.command('transfer')
@click.option('--to_address', type=str, help="the receiver address in BSC", prompt='Enter the receiver address in BSC')
@click.option('--amount', type=str, help="the amount to be sent", default="",
              prompt='Enter the amount to be sent')
def transfer(to_address, amount):
    click.echo(f"{amount}")


bank.add_command(balance)
bank.add_command(transfer)
()