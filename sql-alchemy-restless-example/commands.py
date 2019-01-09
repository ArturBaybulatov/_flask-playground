import random

from create_app import create_app
import models

app = create_app()


@app.cli.command()
def initdb():
    models.db.create_all();


@app.cli.command()
def dropdb():
    models.db.drop_all();


@app.cli.command()
def generate_data():
    categories = []

    for i in range(1, 11):
        categories.append(models.Category(name='Category-%s' % i))

    for i in range(1, 101):
        models.db.session.add(models.Note(
            name='Note-%s' % i,
            private=random.choice((True, False)),
            share_count=random.randint(0, 9999),
            category=random.choice(categories),
        ))

    models.db.session.commit()
