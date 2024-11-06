# [generated]
# by = { compiler = "ecoscope-workflows-core", version = "9999" }
# from-spec-sha256 = "6581c63822e13f69ae1b49518ecca8fd71c6ab4f149fa76fd14fcc3fd3ca48e7"


from io import TextIOWrapper

import click
import ruamel.yaml

from .dispatch import dispatch
from .params import Params


@click.command()
@click.option(
    "--config-file",
    type=click.File("r"),
    required=True,
    help="Configuration parameters for running the workflow.",
)
@click.option(
    "--execution-mode",
    required=True,
    type=click.Choice(["async", "sequential"]),
)
@click.option(
    "--mock-io/--no-mock-io",
    is_flag=True,
    default=False,
    help="Whether or not to mock io with 3rd party services; for testing only.",
)
def main(
    config_file: TextIOWrapper,
    execution_mode: str,
    mock_io: bool,
) -> None:
    yaml = ruamel.yaml.YAML(typ="safe")
    params = Params(**yaml.load(config_file))

    result = dispatch(execution_mode, mock_io, params)

    print(result)


if __name__ == "__main__":
    main()
