install mysql,django,mysql connector,python
install mysql client (if needed)


django-admin startproject mysite


python manage.py startapp polls


change the database name,password in setting.py of django project according to the database your created in in mysql database.

change the static path for static files in setting.py.


python manage.py makemigrations
python manage.py migrate
python manage.py runserver



