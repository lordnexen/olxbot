import os

basedir= os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'..','adws.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True


API_KEY = "1898045745:AAGTqPpJEXDvSXeCXFwndA3pap3dTrkbQ9Y"