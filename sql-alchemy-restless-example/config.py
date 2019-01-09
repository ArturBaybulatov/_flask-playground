import os

basedir = os.path.abspath(os.path.dirname(__file__))

#SECRET_KEY = 's3cr3t666'

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:12345678@localhost/SqlAlchemyTestDb'

SQLALCHEMY_TRACK_MODIFICATIONS = False
