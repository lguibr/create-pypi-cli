# -*- coding: utf-8 -*-
import os
import shutil
import subprocess

import click
from pkg_resources import resource_filename


@click.command()
@click.argument("project_name")
def main(project_name):
    create_pypi_cli(project_name)


def create_pypi_cli(project_name):
    # Create project directory
    os.makedirs(project_name)

    # Create the internal code directory
    os.makedirs(os.path.join(project_name, project_name.replace("-", "_")))

    # Copy the template files
    template_dir = resource_filename("create_pypi_cli", "templates")
    for item in os.listdir(template_dir):
        src_path = os.path.join(template_dir, item)
        dst_path = os.path.join(project_name, item)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
        elif os.path.isdir(src_path):
            shutil.copytree(src_path, dst_path)

    # Update the project name in the setup.py file
    setup_file_path = os.path.join(project_name, "setup.py")
    with open(setup_file_path, "r") as setup_file:
        setup_content = setup_file.read()
    setup_content = setup_content.replace("create-pypi-cli", project_name)
    with open(setup_file_path, "w") as setup_file:
        setup_file.write(setup_content)

    # Create the CLI file
    cli_file_path = os.path.join(
        project_name,
        project_name.replace("-", "_"),
        "cli.py",
    )
    with open(cli_file_path, "w") as cli_file:
        cli_file.write(
            f"""import click

@click.command()
def main():
    click.echo("Hello, {project_name}!")


if __name__ == "__main__":
    main()
"""
        )

    # Initialize git repository
    subprocess.run(["git", "init"], cwd=project_name)


if __name__ == "__main__":
    main()
