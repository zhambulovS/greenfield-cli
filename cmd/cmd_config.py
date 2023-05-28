import click
from dotenv import set_key


@click.command()
@click.option('-rpc', '--rpc_addr', type=str, help='Change Greenfield chain client RPC address',
              prompt='Enter RPC address')
@click.option('-cid', '--chain_id', type=str, help='Change Greenfield chain ID', prompt='Enter chain ID')
@click.option('-pwf', '--password_file', type=str,
              help='Change password file for encrypting and decoding the private key',
              required=False)
def config(rpc_addr, chain_id, password_file):
    if rpc_addr is not None:
        set_key('../.env', 'RPC_ADDR', rpc_addr)
    if chain_id is not None:
        set_key('../.env', 'CHAIN_ID', chain_id)
    if password_file is not None:
        set_key('../.env', 'PASSWORD_FILE', password_file)
