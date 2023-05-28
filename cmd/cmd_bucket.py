import click

from utils import CmdEnumValue


@click.group('bucket')
def bucket():
    pass


@click.command('create')
@click.option('--primary_sp', default="", type=str, help="Indicate the primarySP address, using the string type",
              required=False)
@click.option('--payment_address', default="", type=str, help="indicate the PaymentAddress info, using the string type",
              prompt="Enter the PaymentAddress info, using the string type")
@click.option('--charge_quota', default=0, type=int, help="Indicate the read quota info of the bucket", required=False)
@click.option('--visibility', default='private', type=CmdEnumValue, help="Indicate the read quota info of the bucket",
              required=False)
@click.argument('bucket_url')
def create(bucket_url, primary_sp, payment_address, charge_quota, visibility):
    click.echo(f"{bucket_url}")


@click.command('update')
@click.option('--payment_address', default="", type=str, help="indicate the PaymentAddress info, using the string type",
              prompt="Enter the PaymentAddress info, using the string type")
@click.option('--charge_quota', default=0, type=int, help="Indicate the read quota info of the bucket", required=False)
@click.option('--visibility', default='private', type=CmdEnumValue, help="Indicate the read quota info of the bucket",
              required=False)
@click.argument('bucket_url')
def update(bucket_url,  payment_address, charge_quota, visibility):
    click.echo(f"{bucket_url}")

@click.command('ls')
@click.argument('bucket_url')
def ls(bucket_url):
    click.echo(f"{bucket_url}")


@click.command('delete')
@click.argument('bucket_url')
def delete(bucket_url):
    click.echo(f"{bucket_url}")


@click.command('head')
@click.argument('bucket_url')
def head(bucket_url):
    click.echo(f"{bucket_url}")


bucket.add_command(create)
bucket.add_command(update)
bucket.add_command(ls)
bucket.add_command(head)
bucket.add_command(delete)
