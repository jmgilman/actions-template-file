import click
import os


@click.command()
@click.option(
    "--template",
    default=lambda: os.environ.get("INPUT_TEMPLATE", ""),
    help="Template file to use",
)
@click.option(
    "--parameters",
    default=lambda: os.environ.get("INPUT_PARAMETERS", ""),
    help="Parameters to use when generating from the template",
)
def main(template: str, parameters: str):
    print(template)
    print(parameters)
    pass


if __name__ == "__main__":
    main()
