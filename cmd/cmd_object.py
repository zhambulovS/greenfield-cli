import click

from utils import CmdEnumValue


@click.group('object')
def object():
    pass


@click.command('put')
@click.option('--secondary_sp', type=str,
              help="indicate the Secondary SP addr string list, input like addr1,addr2,addr3", required=False)
@click.option('--content_type', type=str, help="indicate object content-type", required=False)
@click.option('--visibility', default='private', type=CmdEnumValue, help="set visibility of the object",
              required=False)
@click.option('--folder', default='', type=str, help="indicate folder in bucket to which the object will be uploaded",
              required=False)
@click.argument('file_path')
@click.argument('object_url')
def put(secondary_sp, content_type, visibility, folder, file_path, object_url):
    click.echo(f"{file_path}")


@click.command('create-folder')
@click.option('--visibility', default='private', type=CmdEnumValue, help="set visibility of the object",
              required=False)
@click.option('--object_prefix', default='', type=str, help="The prefix of the folder to be created",
              required=False)
@click.argument('object_url')
def create_folder(object_prefix, visibility, object_url):
    click.echo(f"{object_url}")


@click.command('get-object')
@click.option('--start_offset', default=0, type=int, help="start offset info of the download body",
              required=False)
@click.option('--end_offset', default=0, type=int, help="end offset info of the download body",
              required=False)
@click.argument('file_path')
@click.argument('object_url')
def get_object(end_offset, start_offset, object_url):
    click.echo(f"{object_url}")


@click.command('cancel')
@click.argument('object_url')
def cancel(object_url):
    click.echo(f"{object_url}")


@click.command('ls')
@click.argument('bucket_url')
def ls(bucket_url):
    click.echo(f"{bucket_url}")


@click.command('put-object-policy')
@click.option('--group_id', default=0, type=int, help="the group id of the group", required=False)
@click.option('--grantee', default="", type=str, help="the address hex string of the grantee", required=False)
@click.option('--actions', default="", type=str, help="set the actions of the policy," +
                                                      "actions can be the following: create, delete, copy, get, execute, list or all" +
                                                      ", multi actions like \"delete,copy\" is supported",
              required=True)
@click.option('--folder', default='', type=str, help="indicate folder in bucket to which the object will be uploaded",
              required=False)
@click.option('--effect', default='allow', type=CmdEnumValue, help="set the effect of the policy",
              required=False)
@click.option('--expire_time', default=0, type=int, help="set the expire unix time stamp of the policy", required=False)
@click.argument('object_url')
def put_object_policy(group_id, grantee, actions, folder, effect, expire_time, object_url):
    click.echo(f"{object_url}")


@click.command('put-bucket-policy')
@click.option('--group_id', default=0, type=int, help="the group id of the group", required=False)
@click.option('--grantee', default="", type=str, help="the address hex string of the grantee", required=False)
@click.option('--actions', default="", type=str, help="set the actions of the policy," +
                                                      "actions can be the following: create, delete, copy, get, execute, list or all" +
                                                      ", multi actions like \"delete,copy\" is supported",
              required=True)
@click.option('--folder', default='', type=str, help="indicate folder in bucket to which the object will be uploaded",
              required=False)
@click.option('--effect', default='allow', type=CmdEnumValue, help="set the effect of the policy",
              required=False)
@click.option('--expire_time', default=0, type=int, help="set the expire unix time stamp of the policy", required=False)
@click.argument('object_url')
def put_bucket_policy(group_id, grantee, actions, folder, effect, expire_time, object_url):
    click.echo(f"{object_url}")


@click.command('update')
@click.option('--visibility', default='private', type=CmdEnumValue, help="set visibility of the object",
              required=False)
@click.argument('object_url')
def update(visibility, object_url):
    click.echo(f"{object_url}")


@click.command('get-progress')
@click.argument('object_url')
def get_progress(object_url):
    click.echo(f"{object_url}")


@click.command('head')
@click.argument('object_url')
def head(object_url):
    click.echo(f"{object_url}")


@click.command('hash')
@click.argument('file_path')
def hash(file_path):
    click.echo(f"{file_path}")


@click.command('delete')
@click.argument('object_url')
def delete(object_url):
    click.echo(f"{object_url}")


object.add_command(head)
object.add_command(hash)
object.add_command(put)
object.add_command(update)
object.add_command(create_folder)
object.add_command(get_object)
object.add_command(get_progress)
object.add_command(cancel)
object.add_command(ls)
object.add_command(delete)


@click.group('policy')
def policy():
    pass


policy.add_command(put_object_policy)
policy.add_command(put_bucket_policy)
