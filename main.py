# -*- coding: utf-8 -*-
import os
import shutil
import subprocess
import sys


def create_pypi_cli(project_name):
    # Create project directory
    os.makedirs(project_name)

    # Create the internal code directory
    os.makedirs(os.path.join(project_name, project_name.replace("-", "_")))

    # Copy the GitHub Actions workflow file
    os.makedirs(os.path.join(project_name, ".github", "workflows"))
    shutil.copy(
        ".github/workflows/main.yml",
        os.path.join(project_name, ".github", "workflows", "main.yml"),
    )

    # Update the project name in the workflow file
    with open(
        os.path.join(
            project_name,
            ".github",
            "workflows",
            "main.yml",
        ),
        "r",
    ) as f:
        workflow_content = f.read()
    workflow_content = workflow_content.replace(
        "create-pypi-cli",
        project_name,
    )
    with open(
        os.path.join(
            project_name,
            ".github",
            "workflows",
            "main.yml",
        ),
        "w",
    ) as f:
        f.write(workflow_content)

    # Copy the requirements file
    shutil.copy(
        "requirements.txt",
        os.path.join(
            project_name,
            "requirements.txt",
        ),
    )

    # Copy the .gitignore file
    shutil.copy(".gitignore", os.path.join(project_name, ".gitignore"))

    # Copy the pre-commit config file
    shutil.copy(
        ".pre-commit-config.yaml",
        os.path.join(project_name, ".pre-commit-config.yaml"),
    )

    # Copy the isort config file
    shutil.copy(".isort.cfg", os.path.join(project_name, ".isort.cfg"))

    # Copy the setup.py file
    shutil.copy("setup.py", os.path.join(project_name, "setup.py"))

    # Copy the README.md file
    shutil.copy("README.md", os.path.join(project_name, "README.md"))

    # Update the project name in the setup.py file
    with open(os.path.join(project_name, "setup.py"), "r") as f:
        setup_content = f.read()
    setup_content = setup_content.replace("create-pypi-cli", project_name)
    with open(os.path.join(project_name, "setup.py"), "w") as f:
        f.write(setup_content)

    # Create the CLI file
    cli_file_path = os.path.join(
        project_name,
        project_name.replace("-", "_"),
        "cli.py",
    )
    with open(cli_file_path, "w") as f:
        f.write(
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
    if len(sys.argv) != 2:
        print("Usage: python main.py <project_name>")
        sys.exit(1)

    project_name = sys.argv[1]
    create_pypi_cli(project_name)
