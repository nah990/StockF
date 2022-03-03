from rest_framework import serializers
from stock.models import *
from users.models import *

class StockByDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockByDate
        fields = '__all__'


class StockInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockInfo
        fields = '__all__'


class SourceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceInfo
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        
class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['email', 'role', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}