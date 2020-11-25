# -*- coding: utf-8 -*-

import os
import tempfile

from os.path import abspath, dirname, join

_cwd = dirname(abspath(__file__))


class BaseConfiguration(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(_cwd, 'flask-tracking.db')
    SQLALCHEMY_ECHO = False
    HASH_ROUNDS = 100000
    # Pagination setting
    ROWS_PER_PAGE = 30
    # PRAETORIAN CONFIG
    SECRET_KEY = 'flask-session-insecure-secret-key' # TODO: change this to something hard
    JWT_ALGORITHM = 'HS256'
    JWT_ALLOWED_ALGORITHMS = ['HS256']
    JWT_ACCESS_LIFESPAN = {'hours': 24} # the token can only access the api for 24 hours
    JWT_REFRESH_LIFESPAN = {'days': 30} # refreshes every 30 days
    # basic auth config
    BASIC_AUTH_USERNAME = 'kmsb'
    BASIC_AUTH_PASSWORD = 'kmsb'
    BASIC_AUTH_FORCE = False
    # admin
    FLASK_ADMIN_SWATCH = 'cerulean'

class TestConfiguration(BaseConfiguration):
    TESTING = True
    WTF_CSRF_ENABLED = False
    # we will run test in a sqlite in memory
    # + join(_cwd, 'testing.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

    # Since we want our unit tests to run quickly
    # we turn this down - the hashing is still done
    # but the time-consuming part is left out.
    HASH_ROUNDS = 1


class DevelopmentConfiguration(BaseConfiguration):
    DEBUG = True


class StagingConfiguration(BaseConfiguration):
    DEBUG = False


class ProductionConfiguration(BaseConfiguration):
    DEBUG = False
