from flask_restless import APIManager

import models


manager = APIManager()


def set_endpoints(app):
    with app.app_context():
        notes = manager.create_api(
            models.Note,
            methods=('GET', 'POST', 'DELETE'),
            collection_name='notes',
            include_columns=('id', 'name', 'private', 'share_count', 'category'),
            app=app,
        )

        categories = manager.create_api(
            models.Category,
            methods=('GET', 'POST', 'DELETE'),
            collection_name='categories',
            include_columns=('id', 'name'),
            app=app,
        )
