"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
import datetime
app = Flask(__name__)

from crud_blueprint import crud_blueprint
app.register_blueprint(crud_blueprint)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

import logginghelper as logger
logger.init()

import confighelper as config
config.init()

print('done')

@app.route('/')
def hello():
    """Renders a sample page."""
    return "Hello World!"



if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    PORT = 5555
    app.run(HOST, PORT)
