import utils.defines

def configure(app):
    app.config['DEBUG'] = False
    app.config['TESTING'] = False
    app.config['CSRF_ENABLED'] = True
    app.config['SECRET_KEY'] = ''
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///wordcount_dev'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False