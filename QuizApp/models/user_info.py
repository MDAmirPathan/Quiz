from codecs import unicode_escape_decode
from enum import unique
from xmlrpc.client import Boolean
from django.db import models

# Create your models here.

class UserData(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30, default=None, null=False, blank=False )
    last_name = models.CharField(max_length=30, default=None, null=True, blank=True )
    email = models.EmailField(max_length=100, default=None, null=False, blank=False, unique=True )
    password = models.CharField(max_length=255, default=None, null=False, blank=False )

    def __str__(self) -> str:
        return self.email
    
    def register(self) -> None:
        self.save()
    
    def isExists(email) -> Boolean:
        if UserData.objects.filter(email=email):
            return True
        return False