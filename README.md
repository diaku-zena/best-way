
username: admin
password: admin123

python -m venv venv   #install virtual enviroment
venv\scripts\activate   #activate virtual enviroment venv
pip install -r requirements.txt #install required packages
python manage.py migrate # run first migration
python manage.py runserver # run the server

Then locate http://172.0.0.1:8000

## Admin Login

username: admin
password: admin123
