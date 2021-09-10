import os

class Config(object):
    SECRET_KEY = 'santijunco'

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_SSL = False
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'juncosantiago11@gmail.com'
    MAIL_PASSWORD = 'wohxdaxfqklpdiic' # recomendable colocarlo en variable de entorno

class DevelopmentConfig(Config):
    DEBUG = True