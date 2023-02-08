from flask import render_template, session, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash

from . import archive
#from .models import db, User
#from .forms import SignupForm
from flask_login import login_user, login_required, logout_user
from .. import login_manager
import os, shutil
#import pandas as pd

#APP_ROOT = os.path.dirname(os.path.abspath(__file__))
#APP_STATIC = os.path.join(app_instance_path,'static')


@archive.route('/archive', methods=['GET','POST'])
@login_required
def filelist():
	
	if request.method == 'POST':
		flist=request.form.getlist("check")
		print(flist)
		for file in flist:
			src = os.path.join("X:","DCCM Scans",file)
			filename = request.form.get("filename") 
			dst = os.path.join("X:","NPP Docs","NPP",filename)
			os.mkdir(dst)
			dst = os.path.join(dst,filename + ".pdf")
			shutil.copyfile(src, dst)
			os.remove(src)
	path = os.path.join("X:","DCCM Scans")
	lst = os.listdir(path)
	return render_template('archive.html',lst=lst,path=path)

#@archive.route('/transfer')
#def transfer():
	#filenames=request.form.getlist('check')
	#print(filenames)
	#return redirect(url_for('archive.archive'))
