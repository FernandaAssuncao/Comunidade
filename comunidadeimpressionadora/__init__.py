from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)



app.config['SECRET_KEY'] = 'f9ab251b33ddc6b6a99747b1d5cae5a1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comuinidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Faça login ou crie sua conta para vizualizar está pagina'
login_manager.login_message_category = 'alert-info'

from comunidadeimpressionadora import routes

