import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

	@staticmethod
	def init_app(app):
		pass
class ProdConfig(Config):
	pass
class DevConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

config = {
	'development': DevConfig,
	'production': ProdConfig,
	'default': DevConfig
}
