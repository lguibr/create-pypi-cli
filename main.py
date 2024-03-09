# -*- coding: utf-8 -*-
import os
import subprocess
from importlib import resources

import click

import templates


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
    for file_name in [
        "requirements.txt",
        ".gitignore",
        ".pre-commit-config.yaml",
        ".isort.cfg",
        "setup.py",
        "README.md",
    ]:
        file_content = resources.read_text(templates, file_name)
        with open(os.path.join(project_name, file_name), "w") as file:
            file.write(file_content)

    # Update the project name in the setup.py file
    setup_file_path = os.path.join(project_name, "setup.py")
    with open(setup_file_path, "r") as setup_file:
        setup_content = setup_file.read()
    setup_content = setup_content.replace("create-pypi-cli", project_name)
    with open(setup_file_path, "w") as setup_file:
        setup_file.write(setup_content)

    # Create the .github/workflows directory
    os.makedirs(os.path.join(project_name, ".github", "workflows"))

    # Copy the main.yml file to .github/workflows
    main_yml_content = resources.read_text(templates, "workflows/main.yml")
    with open(
        os.path.join(project_name, ".github", "workflows", "main.yml"), "w"
    ) as file:
        file.write(main_yml_content)

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
