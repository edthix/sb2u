# konelayan-api
Ko-Nelayan API using Flask Python

## Installation

1. Create virtual environment (using Python 3). `python -m venv lms-env`
2. Activate the environment everytime you want to develop the app. `source lms-env/bin/activate`
3. Pip install requirements. `pip install -r requirements.txt`

## Configuration

1. Edit in `instance/config.py` by following these examples:

```
import os
import tempfile

SECRET_KEY = ''
DEBUG = True
ENV = 'development'

# DATABASE
DBUSER = 'root'
DBPASSWORD = ''
DBHOST = 'localhost'
DBNAME = 'konelayan_lms_webapi_dev'

SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}/{}'.format(
    DBUSER, DBPASSWORD, DBHOST, DBNAME)
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

## Migration

1. Declare our models (e.g models/user.py)
2. Import models in `lms/__init__.py`
3. run `$FLASK_APP=lms flask db init` to iniatiate
4. run `$FLASK_APP=lms flask db migrate` to run a migration
5. run `$FLASK_APP=lms flask db upgrade` to apply

## How to run the server?

1. Inside the directory `konelayan-lms-webapi` run this command
2. `$FLASK_APP=lms python -m flask run`

## Formatting code

1. We will need to run `autopep8` on our files to make it prettier
2. Run these commands inside `konelayan-lms-webapi` folder

```
$autopep8 --in-place --aggressive --aggressive *.py
$autopep8 --in-place --aggressive --aggressive */*.py
```

## Adding Docker Support

1. Download docker install script
```
curl -fsSL https://get.docker.com -o get-docker.sh
```
2. Run the bash script
```
sh get-docker.sh
```
3. Download docker compose and chmod the docker-compose executable
```
curl -L https://github.com/docker/compose/releases/download/1.25.4/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
```
4. Copy docker-compose-sample.yaml to docker-compose.yaml
5. Add in your password for the database in the docker-compose.yaml
6. Run docker compose build to build our Flask API into an image
```
sudo docker-compose build
```
7. Run the command below to create the containers and run in detached mode
```
sudo docker-compose up -d
```
8. Run the following commands in order to create database migrations and upgrade the database
```
sudo docker exec lms-api flask db migrate
sudo docker exec lms-api flask db upgrade
```
## Flask Monitoring Configuration

1. Edit/Create `instance/flask_monitoring_dashboard_config.cfg`, below are examples:

```
[dashboard]
APP_VERSION:1.0
CUSTOM_LINK:monitordashboard
MONITOR_LEVEL:1
OUTLIER_DETECTION_CONSTANT:2.5
SAMPLING_PERIOD:20
ENABLE_LOGGING:True

[authentication]
USERNAME:username
PASSWORD:password
GUEST_USERNAME:guest
GUEST_PASSWORD:['dashboardguest!', 'second_pw!']
SECURITY_TOKEN:cc83733cb0af8b884ff6577086b87909

[database]
TABLE_PREFIX:fmd
DATABASE:mysql://<user>:<password>@192.168.0.1:3306/database_name

[visualization]
TIMEZONE:Asia/Kuching
COLORS:{'main':'[0,97,255]',
	'static':'[255,153,0]'}
```
## Unit test
