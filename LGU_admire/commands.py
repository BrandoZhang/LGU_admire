import click

from LGU_admire import app, db
from LGU_admire.models import Message


@app.cli.command()
@click.option("--drop", is_flag=True, help="Create after drop.")
def initdb(drop):
    """Initialize the database."""
    pass



@app.cli.command()
@click.option("--count", default=20, help="Quantity of messages, default is 20.")
def forge(count):
    """Generate fake messages."""
    from faker import Faker
    pass
