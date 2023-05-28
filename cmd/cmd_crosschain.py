import click


@click.group()
def crosschain():
    pass


@click.command('transfer')
@click.option('-ta', '--to_address', type=str, help="Enter receiver address in BSC",
              prompt="Enter receiver address in BSC")
@click.option('-amt', '--amount', type=str, help="Enter amount of BNB to be sent",
              prompt="Enter amount of BNB to be sent")
def transfer(to_address, amount):
    message = f"To Address: {to_address}\nAmount: {amount}"
    click.echo(message)


@click.command('mirror')
@click.option('-rsc', '--resource', type=str, help="Resource type(group, bucket, object)",
              prompt="Enter resource type(group, bucket, object)")
@click.option('-rsc_id', '--resource_id', type=str, help='Resource id', prompt="Enter resource id")
def mirror(resource, resource_id):
    click.echo(resource, resource_id)


crosschain.add_command(mirror)

crosschain.add_command(transfer)
