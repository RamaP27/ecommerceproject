from django.db import models


class User(models.Model):
    title = models.CharField(max_length=100, choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms')], default='Mr')
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, default='scaler@scaler.com')
    address = models.CharField(max_length=255, default='Unknown Address')
