from django.db import models

class Data(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
