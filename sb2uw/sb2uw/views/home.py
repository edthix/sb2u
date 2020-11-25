# -*- coding: utf-8 -*-

from flask import (
    Blueprint,
    render_template)

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    """
    Display an empty or welcome page
    """
    return render_template('home/index.html')
