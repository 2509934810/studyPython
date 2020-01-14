from django.db import models
from rest_framework import serializers
# Create your models here.


class Message(models.Model):
    subject = models.CharField(max_length=30)
    body = models.TextField()
    
class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'subject', 'body', 'pk')
