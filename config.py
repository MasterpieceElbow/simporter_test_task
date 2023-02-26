class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = "1g90ekG1EEgwkn34gn2wg"
    SQLALCHEMY_DATABASE_URI = "sqlite:///./production.db"
    

class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///./project.db"
