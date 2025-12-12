cd /var/www/flaskapp
source venv/bin/activate
nohup python3 app.py > flask.log 2>&1 &