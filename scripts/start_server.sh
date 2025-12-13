
cd /var/www/flask

if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

source venv/bin/activate

pip install -r requirement.txt

nohup python3 app.py > flask.log 2>&1 &
