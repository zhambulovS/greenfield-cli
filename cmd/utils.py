import binascii
import datetime

from dotenv import dotenv_values
from eth_utils import ValidationError

# data format
iso8601DateFormatSecond = "%Y-%m-%dT%H:%M:%S"

# constants
maxFileSize = 2 * 1024 * 1024 * 1024
maxListObjects = 100
publicReadType = "public-read"
privateType = "private"
inheritType = "inherit"
effectAllow = "allow"
effectDeny = "deny"
primarySPFlag = "primarySP"
chargeQuotaFlag = "chargedQuota"
visibilityFlag = "visibility"
paymentFlag = "paymentAddress"
secondarySPFlag = "secondarySPs"
contentTypeFlag = "contentType"
startOffsetFlag = "start"
endOffsetFlag = "end"
initMemberFlag = "initMembers"
addMemberFlag = "addMembers"
removeMemberFlag = "removeMembers"
groupOwnerFlag = "groupOwner"
headMemberFlag = "headMember"
groupIDFlag = "groupId"
granteeFlag = "grantee"
actionsFlag = "actions"
effectFlag = "effect"
expireTimeFlag = "expire"
ownerAddressFlag = "owner"
addressFlag = "address"
toAddressFlag = "toAddress"
fromAddressFlag = "fromAddress"
amountFlag = "amount"
resourceFlag = "resource"
IdFlag = "id"
objectPrefix = "prefix"
folderFlag = "folder"
defaultKeyfile = "key.json"
defaultPasswordfile = "password"
privKeyFileFlag = "privKeyFile"
passwordFileFlag = "passwordfile"
EncryptScryptN = 1 << 18
EncryptScryptP = 1
ErrBucketNotExist = 'bucket not exist'
ErrObjectNotCreated = "object not created on chain"
ErrObjectSeal = "object not sealed before downloading"
ErrGroupNotExist = "group not exist"
ErrFileNotExist = "file path not exist"


class CmdEnumValue:
    def __init__(self, enum, default):
        self.enum = enum
        self.default = default
        self.selected = ""

    def set(self, value):
        if value in self.enum:
            self.selected = value
            return None
        return "allowed values are {}".format(", ".join(self.enum))

    def __str__(self):
        if self.selected == "":
            return self.default
        return self.selected


def to_cmd_err(err):
    print("run command error:", str(err))
    return None


def gen_cmd_err(msg):
    print("run command error:", msg)
    return None


def parse_chain_info(info, is_bucket_info):
    if is_bucket_info:
        print("latest bucket info:")
    else:
        print("latest object info:")

    info_str = info.split(" ")
    for info in info_str:
        if "create_at:" in info:
            time_info = info.split(":")
            timestamp = int(time_info[1])
            dt = datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc)
            t = dt.astimezone(datetime.timezone(datetime.timedelta(hours=8)))
            info = time_info[0] + ":" + t.strftime(iso8601DateFormatSecond)
        if "checksums:" in info:
            hash_info = info.split(":")
            info = hash_info[0] + ":" + binascii.hexlify(hash_info[1].encode()).decode()
        print(info)


# get password
def get_password(config):
    filepath = ""
    if config.PasswordFile != "":
        filepath = config.PasswordFile
    else:
        filepath = "password.txt"

    try:
        with open(filepath, "r") as file:
            password_content = file.read().strip()
            return password_content, None
    except (FileNotFoundError, IOError) as e:
        return "", FileNotFoundError(f"Failed to read password file: {str(e)}")


# load_key loads a secp256k1 private key from the given file.
def load_key(file):
    try:
        with open(file, "r") as fd:
            key_data = fd.read().strip()
        return key_data

    except (FileNotFoundError, IOError) as e:
        return "", None, FileNotFoundError(f"Failed to open key file: {str(e)}")
    except (ValueError, ValidationError) as e:
        return "", None, ValueError(f"Failed to load private key: {str(e)}")


class CmdConfig:
    def __init__(self):
        self.RpcAddr = ""
        self.ChainId = ""
        self.PasswordFile = ""
        self.Host = ""


def parse_config_file(file_path):
    config = CmdConfig()
    try:
        env_values = dotenv_values(file_path)
        config.RpcAddr = env_values.get("RPC_ADDR", "")
        config.ChainId = env_values.get("CHAIN_ID", "")
        config.PasswordFile = env_values.get("PASSWORD_FILE", "")
        config.Host = env_values.get("HOST", "")
        return config
    except Exception as e:
        return None, ValueError("failed to parse config file: {}".format(str(e)))
