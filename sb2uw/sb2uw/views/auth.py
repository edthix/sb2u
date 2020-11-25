# -*- coding: utf-8 -*-

import functools

from flask import (
    Blueprint,
    Response,
    current_app,
    flash,
    g,
    jsonify,
    make_response,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['GET'])
def login():
    return render_template('auth/login.html')

@bp.route('/login', methods=['POST'])
def do_login():
    email = request.form['email']
    session['username'] = email
    print(session['username'])
    return redirect(url_for('home.index'))


@bp.route('/register', methods=['GET'])
def register():
    return render_template('auth/register.html')

@bp.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    if 'username' in session:
        print(session['username'])
    return redirect(url_for('home.index'))
