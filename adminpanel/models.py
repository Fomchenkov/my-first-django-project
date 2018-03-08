from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
