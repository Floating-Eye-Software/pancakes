import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask
from flask_login import LoginManager
from auth import auth
from data import db
from public import public
from user import user

# SECRET_KEY is the flask session key read from .env
# import random, string
# ''.join(random.choices(string.ascii_letters + string.digits, k=16))
load_dotenv(find_dotenv())

app = Flask(__name__, static_folder='static', static_url_path='')
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.register_blueprint(auth)
app.register_blueprint(public)
app.register_blueprint(user)
db.create_users_table()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(username):
    return db.get_user(username)

if __name__ == '__main__':
    app.run()
