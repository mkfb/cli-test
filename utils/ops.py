import click
from utils.base import CLIBase
from utils.commands import DeployCLI, UpdateCLI, RollbackCLI

@click.group()
@click.option('--config', required=True, type=click.Path(exists=True))
@click.option('--env', required=True, type=str)
@click.option('--verbose', is_flag=True, default=False)
@click.option('--log', required=False, default="cli.log", type=click.Path())
@click.option('--secret', required=False, type=str)
@click.pass_context
def cli(ctx, config, env, verbose, log, secret):
    ctx.obj = CLIBase(config, env, verbose, log, secret)

@cli.command()
@click.pass_obj
def deploy(obj):
    cli = DeployCLI(obj.config_path, obj.environment, obj.verbose, obj.log_path, obj.secret)
    cli.run()

@cli.command()
@click.pass_obj
def update(obj):
    cli = UpdateCLI(obj.config_path, obj.environment, obj.verbose, obj.log_path, obj.secret)
    cli.run()

@cli.command()
@click.pass_obj
def rollback(obj):
    cli = RollbackCLI(obj.config_path, obj.environment, obj.verbose, obj.log_path, obj.secret)
    cli.run()
