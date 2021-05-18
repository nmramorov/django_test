from api.models import User, Friendship
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'second_name', 'additional_info']


class FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = ['first_user', 'second_user', 'start_date']
