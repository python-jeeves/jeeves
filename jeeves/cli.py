import subprocess

import typer

app = typer.Typer()


# noinspection PyShadowingBuiltins
@app.command()
def format(project_directory: str):
    """Auto format the project."""
    subprocess.run(['isort', project_directory])


@app.command()
def lint(project_directory: str):
    """Lint the project."""


if __name__ == '__main__':
    app()
