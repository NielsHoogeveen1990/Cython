import click
import logging
from Cython_app.Sub_package.calculate_primes import calculate_primes

logger = logging.getLogger(__name__)


@click.group()
def main():
    logging.basicConfig(level=logging.INFO)
    pass


@main.command()
@click.option("--nb-primes", type=int)
def cli_primes(nb_primes):
    calculate_primes(nb_primes)
    logger.info('Finished with executing code.')
