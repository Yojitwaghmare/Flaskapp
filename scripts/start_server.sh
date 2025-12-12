#!/bin/bash

export DB_HOST="flaskapp-mydb-uzt9cdqml1vy.cruqqgmqsn5d.ap-south-1.rds.amazonaws.com"
export DB_USER="admin"
export DB_PASSWORD="password"
export DB_NAME="dectobinary"

cd /var/www/flaskapp

if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

source venv/bin/activate

pip install -r requirement.txt

nohup python3 app.py > flask.log 2>&1 &
