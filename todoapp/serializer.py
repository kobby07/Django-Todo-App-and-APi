from rest_framework import serializers
from .models import mytodo
from django.contrib.auth.models import User



class todoserializer(serializers.ModelSerializer):
    class Meta:
        model=mytodo
        fields=['task']

class ListTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=mytodo
        fields='__all__'

