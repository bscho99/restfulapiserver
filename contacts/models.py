from django.db import models
import uuid

# Create your models here.

'''
class Addresses(models.Model):
    name = models.CharField(max_length=10)
    number = models.CharField(max_length=11)
    address = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
'''


class Contact(models.Model):
    name = models.CharField(max_length=30)
    userid = models.CharField(max_length=255, blank=True)
    number = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def get_id(self):
        return self.id
