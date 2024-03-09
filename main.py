# -*- coding: utf-8 -*-
import importlib.resources
import os
import subprocess

import click


@click.command()
@click.argument("project_name")
def main(project_name):
    create_pypi_cli(project_name)


def create_pypi_cli(project_name):
    # Create project directory
    os.makedirs(project_name)

    # Create the internal code directory
    os.makedirs(os.path.join(project_name, project_name.replace("-", "_")))

    # Copy the GitHub Actions workflow file
    os.makedirs(os.path.join(project_name, ".github", "workflows"))
    workflow_content = importlib.resources.read_text(
        "create_pypi_cli", ".github/workflows/main.yml"
    )
    with open(
        os.path.join(project_name, ".github", "workflows", "main.yml"),
        "w",
    ) as f:
        f.write(workflow_content)

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
    requirements_content = importlib.resources.read_text(
        "create_pypi_cli", "requirements.txt"
    )
    with open(
        os.path.join(
            project_name,
            "requirements.txt",
        ),
        "w",
    ) as f:
        f.write(requirements_content)

    # Copy the .gitignore file
    gitignore_content = importlib.resources.read_text(
        "create_pypi_cli",
        ".gitignore",
    )
    with open(os.path.join(project_name, ".gitignore"), "w") as f:
        f.write(gitignore_content)

    # Copy the pre-commit config file
    precommit_content = importlib.resources.read_text(
        "create_pypi_cli", ".pre-commit-config.yaml"
    )
    with open(os.path.join(project_name, ".pre-commit-config.yaml"), "w") as f:
        f.write(precommit_content)

    # Copy the isort config file
    isort_content = importlib.resources.read_text(
        "create_pypi_cli",
        ".isort.cfg",
    )
    with open(os.path.join(project_name, ".isort.cfg"), "w") as f:
        f.write(isort_content)

    # Copy the setup.py file
    setup_content = importlib.resources.read_text(
        "create_pypi_cli",
        "setup.py",
    )
    with open(os.path.join(project_name, "setup.py"), "w") as f:
        f.write(setup_content)

    # Copy the README.md file
    readme_content = importlib.resources.read_text(
        "create_pypi_cli",
        "README.md",
    )
    with open(os.path.join(project_name, "README.md"), "w") as f:
        f.write(readme_content)

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
    main()
