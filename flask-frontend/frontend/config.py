import os


class Config:
    SECRET_KEY = '0917b13a9091915d54b6336f45909539cce452b3661b21f386418a257883b30a'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENDPOINT_ROUTE = 'https://thinger.appspot.com'
    ACCIDENT_COOR_DATA_URL = '/event/acc/all'
    LOG_COOR_URL = '/event/add'
