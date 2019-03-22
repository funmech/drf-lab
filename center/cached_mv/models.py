from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=200)


class Belonging(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)