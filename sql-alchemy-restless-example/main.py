from create_app import create_app


app = create_app()

print(app.url_map) # Debug


# import code; code.interact(local=dict(globals(), **locals()))
