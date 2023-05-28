import click


@click.group('sp')
def sp():
    pass


@click.command('ls')
def ls():
    click.echo("Storage provider list")


@click.command('head')
@click.argument('url')
def head(url):
    click.echo(f"Storage provider info by {url}")


@click.command()
@click.argument('url')
def get_price(url):
    click.echo(f"Quota price by {url}")


sp.add_command(ls)
sp.add_command(head)
sp.add_command(get_price)
