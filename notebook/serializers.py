from rest_framework import serializers
from .models import * 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note 
        fields = ('__all__')

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type 
        fields = ('__all__')
