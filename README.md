
# Setup project

## start/setup venv
`python -m venv env`

## requirements
be sure to install a python virtual environment and install all of the requirements in requirements.txt

`pip install -r requirements.txt`

## .env file
also you need to create a  .env file

in the .env file write the fallowing

SECRET_KEY= your secret key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3 

TIME_ZONE=your timezone, ex: America/New_York

EMAIL_BACKEND=the email backend ex: django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=ex: smtp.gmail.com
EMAIL_HOST_USER=your host email
EMAIL_HOST_PASSWORD=your host password
EMAIL_PORT=your port
EMAIL_USE_TLS=True

## setup database

`python manage.py makemigrations`
`python manage.py makemigrations djbootstrap`
`python manage.py migrate`

## to start 
To run simply run the command
`python manage.py runserver`
