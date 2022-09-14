from datetime import date
from mailbox import NotEmptyError
from operator import mod
from os import urandom
from select import select
from unicodedata import name
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class Webpage(models.Model):
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name =  models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)