# -*- coding: utf-8 -*-

from flask import (
    Blueprint,
    render_template)

bp = Blueprint('members', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    return render_template('members/index.html')
