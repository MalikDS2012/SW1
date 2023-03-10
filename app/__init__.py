from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

db = SQLAlchemy()
bootstrap = Bootstrap()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'main.index'

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)
	
	bootstrap.init_app(app)
	db.init_app(app)
	login_manager.init_app(app)
	
	# attach routes and custom error pages here



	from app.main import main as main_blueprint
	app.register_blueprint(main_blueprint)
	
	from app.auth import auth
	app.register_blueprint(auth)
	
	from app.archive import archive
	app.register_blueprint(archive)


	return app
