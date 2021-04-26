from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from basic_flask.config import Config


app = Flask(__name__)
app.config.from_object(Config)
#app.config['SECRET_KEY'] = '\x8d\x9fI\x18.\x01\x9c7\xec\x0e\xc6\xbc\x0f\xedl\x0c'

from basic_flask import routes