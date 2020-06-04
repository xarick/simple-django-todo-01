# simple-django-todo-01

this django project supports CRUD

The requirements file lists all the libraries used

# Installing

git clone https://github.com/xarick/simple-django-todo-01.git
cd simple-django-todo-01
pip install -r requirements.txt

setting up your database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'username',
        'PASSWORD': 'password',
    }
}

then
python manage.py migrate
python manage.py makemigrations
python manage.py runserver

