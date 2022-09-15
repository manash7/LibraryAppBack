from pyexpat import model
from rest_framework import serializers
from LibraryApp.models import Books, customusers

class BooksSerializers(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields=("id","title","author","category","price")

class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model=customusers
        fields=("id","first","last","email")
