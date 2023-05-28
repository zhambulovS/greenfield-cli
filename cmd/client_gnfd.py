from web3 import Web3, Account

from web3.middleware import geth_poa_middleware

from key import config
from utils import get_password


def new_client(ctx):
    rpc_addr = ctx.get("rpcAddr")
    if not rpc_addr:
        if config and config.get("RpcAddr"):
            rpc_addr = config["RpcAddr"]
        else:
            raise ValueError("Failed to parse rpc address, please set it in the config file")

    chain_id = ctx.get("chainId")
    if not chain_id:
        if config and config.get("ChainId"):
            chain_id = config["ChainId"]
        else:
            raise ValueError("Failed to parse chain id, please set it in the config file")

    keyfile_path = ctx.get("keystore")
    if not keyfile_path:
        keyfile_path = "../key.json"

    # Fetch private key from keystore
    with open(keyfile_path, "r") as keyfile:
        key_json = keyfile.read()

    password = get_password(config)

    private_key = Account.decrypt(key_json, password)

    account = Account.from_key(private_key)

    w3 = Web3(Web3.HTTPProvider(rpc_addr))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    w3.eth.default_account = account.address
    w3.eth.chainId = chain_id

    return w3


def parse_bucket_and_object(url_path):
    if "gnfd://" in url_path:
        url_path = url_path[len("gnfd://"):]

    index = url_path.find("/")

    if index == -1:
        raise ValueError("URL not correct, cannot parse bucket name and object name")

    return url_path[:index], url_path[index + 1:]


def parse_bucket(url_path):
    if "gnfd://" in url_path:
        url_path = url_path.replace("gnfd://", "")

    splits = url_path.split("/", 1)

    return splits[0]
