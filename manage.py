#from app import app, db, User
from app.auth.models import User
from app import db
#@app.shell_context_processor
@shell_context_processor
def make_shell_context():
	#return dict(app=app, db=db, User=User)
	return dict( db=db, User=User)