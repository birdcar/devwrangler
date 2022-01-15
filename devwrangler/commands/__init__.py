"""Devwrangler's CLI package: pydev."""
import typer

from devwrangler.commands.configure import config_app
from devwrangler.commands.create import create_app
from devwrangler.utilities.display import STD_ERR, STD_OUT

app = typer.Typer(name="devwrangler")
app.add_typer(create_app, name='create', invoke_without_command=True)
app.add_typer(config_app, name="configure", invoke_without_command=True)


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """Bringing Peace, Justice, and Security to your Python empire."""
    if ctx.invoked_subcommand is None:
        with STD_OUT.status("Generating environment..."):
            STD_OUT.print("Gathering configuration from environment...")
            STD_ERR.print("NO CONFIGURATION FOUND")
            ctx.invoke(app.registered_groups)
            ctx.invoke(config_app.registered_callback)


if __name__ == '__main__':
    app()
