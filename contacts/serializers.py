from rest_framework import serializers
from .models import Contact

'''
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addresses
        fields = ['name', 'number', 'address']
'''


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'userid', 'name', 'number', 'email']
