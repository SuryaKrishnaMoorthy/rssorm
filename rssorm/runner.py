# External Libraries
import click

# Internal Libraries
from .orm import init_db, User


DB_URI = 'sqlite:///rss.db'


@click.command(name='connect')
def cli():
    c = init_db(DB_URI)

    # test data
    logins = ['jhibba', 'mcarl7', 'staylo']

    # create a set of objects
    users = [User(login=login) for login in logins]

    # add set
    c.add_all(users)
    c.commit()
