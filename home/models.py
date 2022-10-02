import email
from django.db import models

# Create your models here.

#class for sending message by user of website

class Contacts(models.Model):
    fullname = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    message = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return 'Message from' + self.fullname

        