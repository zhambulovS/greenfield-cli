import click


@click.group('group')
def group():
    pass


@click.command('create')
@click.option('--init_member', type=str, default="",
              help="indicate the init member addr string list, input like addr1,addr2,addr3", required=False)
@click.argument('group_url')
def create(init_member, group_url):
    click.echo(f"{group_url}")


@click.command('update')
@click.option('--add_member', type=str, default="",
              help="indicate the init member addr string list, input like addr1,addr2,addr3", required=False)
@click.option('--remove_member', type=str, default="",
              help="indicate the init member addr string list, input like addr1,addr2,addr3", required=False)
@click.option('--group_owner', type=str, default="",
              help="need set the owner address if you are not the owner of the grou", required=False)
@click.argument('group_url')
def update(add_member, group_url, remove_member, group_owner):
    click.echo(f"{group_url}")


@click.command('head-member')
@click.option('--head_member', type=str, default="",
              help="indicate the head member address", required=False)
@click.option('--group_owner', type=str, default="",
              help="need set the owner address if you are not the owner of the grou", required=False)
@click.argument('group_url')
def head_member(head_member, group_url, group_owner):
    click.echo(f"{group_url}")


@click.command('head')
@click.option('--group_owner', type=str, default="",
              help="need set the owner address if you are not the owner of the grou", required=False)
@click.argument('group_url')
def head(group_url, group_owner):
    click.echo(f"{group_url}")


@click.command('delete')
@click.argument('group_url')
def delete(group_url):
    click.echo(f"{group_url}")


group.add_command(head)
group.add_command(head_member)
group.add_command(delete)
group.add_command(update)
group.add_command(create)
