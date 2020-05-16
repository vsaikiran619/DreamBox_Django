# DreamBox_django_project
Features

1) For Django 2.1 and Python 3.7
2) Modern virtual environments with pipenv
3) Styling with Bootstrap v4.1.3
4) posts, interviews, comments model
5) username/password for log in/sign up

First-time setup

1) Make sure Python 3.7x,Pipenv and PostgreSql are already installed.
2) Clone the repo and configure the virtualenv:

	$ git clone https://github.com/Rakeshvarma301/DreamBox_django_project.git
	$ cd web
	$ pipenv install
	$ pipenv shell

Set up the initial migration for our all models in one app and build the database.

	(web) $ python manage.py makemigrations
	(web) $ python manage.py migrate

Create a superuser:
	
	(web) $ python manage.py createsuperuser

Confirm everything is working:

	(web) $ python manage.py runserver
	
Load the site at http://127.0.0.1:8000
