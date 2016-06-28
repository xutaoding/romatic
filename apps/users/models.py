from __future__ import unicode_literals

# from django.db import models
from django.contrib.auth.models import User
from mongoengine import Document
from mongoengine import StringField
from rest_framework import serializers


# Create your models here.
class Users(Document):
    username = StringField(max_length=15)
    password = StringField(max_length=20)

    def __unicode__(self):
        return 'User: <%s>' % self.username


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']




