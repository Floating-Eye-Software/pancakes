import sqlite3
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# https://docs.python.org/3/library/sqlite3.html
# https://flask-login.readthedocs.io/en/0.4.1/

DB_FILENAME = 'data/pancakes.db'

class User(UserMixin):
    def __init__(self, username):
        self.username = username

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username

def create_users_table():
    sql = '''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT NOT NULL COLLATE NOCASE PRIMARY KEY,
            password TEXT NOT NULL
        )
    '''
    conn = sqlite3.connect(DB_FILENAME)
    conn.cursor().execute(sql)
    conn.commit()
    conn.close()

def user_exists(c, username):
    c.execute('SELECT * FROM users WHERE username = ?', [username])
    return (c.fetchone()!=None)

def get_user(username):
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ?', [username])
    result = c.fetchone()
    conn.close()

    if result == None:
        user = None
    else:
        (savedname, _) = result
        user = User(savedname)
    return user

def sign_up_user(username, password):
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    exists = user_exists(c, username)
    if(not exists):
        hash = generate_password_hash(password, method='sha256')
        c.execute('INSERT INTO users VALUES (?, ?)', [username, hash])
    conn.commit()
    conn.close()
    return not exists

def check_password(username, password):
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    c.execute('SELECT password FROM users WHERE username = ?', [username])
    result = c.fetchone()
    if result != None:
        (hash,) = result
    match = (result!=None) and check_password_hash(hash, password)
    conn.close()
    return match

if __name__ == '__main__':
    create_users_table()
    sign_up_user('test@example.com', 'password')
    check_password('TeSt@exAmple.COm', 'password')
    check_password('test@example.com', 'sdvsdvsv')
    user = get_user('test@example.com')
    user.username
    user.is_active()
    user2 = get_user('dsvsdvsdvsdvsdv')
    print(user2)
