import os
basedir = os.path.abspath(os.path.dirname(__file__)) #db dir

class Config: #所有需要config彙整
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string' #使用WTF需要的密鑰
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com') #email 需要的Server port TLS
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
                   ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') #寄件者的帳號密碼 儲存在環境變數中(自己先行設置)
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_SENDER = 'jasperli0407@gmail.com'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config): #SQLite 設置URL
    DEBUG = True
    #獲取環境變量DB的URL 如果獲取到使用os.environ.get('DEV_DATABASE_URL') 如果沒有
    #'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite') 則生成一個新的db
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URL = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}