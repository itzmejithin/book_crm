from django.db import models

# Create your models here.

class Employee(models.Model):
    email=models.EmailField(null=True)
    uname=models.CharField( max_length=30)
    age=models.PositiveIntegerField()
    place=models.CharField( max_length=30)
    
#env\Scripts\activate.bat

# django-admin startproject projectname
# python manage.py runserver
# python manage.py startapp appname
# python manage.py makemigrations
# python manage.py migrate
    
