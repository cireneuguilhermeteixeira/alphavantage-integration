import utils.defines
from utils.defines import POSTGRES_USER, POSTGRES_PW, POSTGRES_URL, POSTGRES_DB

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)

def configure(app):
    app.config['DEBUG'] = False
    app.config['TESTING'] = False
    app.config['CSRF_ENABLED'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False