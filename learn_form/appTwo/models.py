from django.db import models

# Create your models here.
class User(models.Model):
    lastName = models.CharField(max_length=128)
    firstName = models.CharField(max_length=128)
    email = models.EmailField(max_length=256, unique=True)

    def __str__(self):
        return str(self.email)

