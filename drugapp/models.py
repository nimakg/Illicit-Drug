# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Registration(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    pno = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    role=models.IntegerField()
    blocked=models.IntegerField()
class Document(models.Model):
    userid = models.IntegerField()
    hashvalue = models.CharField(max_length=200)
    image_url = models.URLField()
class Notifications(models.Model):
    userid = models.CharField(max_length=5)
    Notification = models.CharField(max_length=200)
    timet = models.CharField(max_length=200)
class Posts(models.Model):
    userid = models.CharField(max_length=5)
    post = models.CharField(max_length=200)
