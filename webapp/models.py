from django.db import models


# Create/Define User Model
class User(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    mobile = models.IntegerField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name
