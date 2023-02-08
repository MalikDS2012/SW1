from flask import Blueprint

archive = Blueprint('archive', __name__,template_folder='../templates/archive')

from . import controllers, errors
