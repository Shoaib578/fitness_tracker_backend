from rest_framework import serializers
from apis.models import User,FitnessSession

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields ='__all__'


class FitnessSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessSession
        fields ='__all__'