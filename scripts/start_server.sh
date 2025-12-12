export DB_HOST="flaskapp-mydb-uzt9cdqml1vy.cruqqgmqsn5d.ap-south-1.rds.amazonaws.com"
export DB_USER="admin"
export DB_PASSWORD="password"
export DB_NAME="dectobinary"

cd /var/www/flaskapp
source venv/bin/activate
nohup python3 app.py > flask.log 2>&1 &