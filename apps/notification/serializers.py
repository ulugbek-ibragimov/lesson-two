from rest_framework import serializers
from apps.notification.models import UserFCMToken, Notification, NotificationUser
from django.contrib.auth.models import User


class FCMTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFCMToken
        fields = ['token', 'user']
        extra_kwargs = {
            'user': {'required': False}
        }

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['title', ]


class CreateNotificationSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Notification
        fields = ['title', 'message', 'is_for_everyone', 'users', 'created_at']
        read_only_fields = ['created_at']

class NotificationUserSendSerializer(serializers.Serializer):
    notification_id = serializers.IntegerField()
    user_id = serializers.IntegerField()