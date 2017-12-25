from flask import Flask
from flask_restful import Api

app = Flask(__name__, instance_relative_config=True)
app.config.from_envvar('ECOMMERCE')

# Initialize Flask-Restful
api = Api(app)

# Initialize MongoEngine
ME = app.config['ME']
ME.init_app(app)

