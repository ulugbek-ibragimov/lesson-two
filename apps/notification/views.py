from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from apps.notification.models import UserFCMToken, Notification, NotificationUser
from apps.notification.serializers import FCMTokenSerializer, CreateNotificationSerializer, NotificationUserSendSerializer
from django.shortcuts import get_object_or_404
from django.utils import timezone
from apps.notification.utils import send_push_notification
from rest_framework.views import APIView
from rest_framework.response import Response

class RegisterFcmToken(CreateAPIView):
    serializer_class = FCMTokenSerializer
    queryset = UserFCMToken.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CreateNotification(CreateAPIView):
    serializer_class = CreateNotificationSerializer
    queryset = Notification.objects.all()


class SendNotification(APIView):
    def post(self, request, notification_id, user_id):
        serializer = NotificationUserSendSerializer(data={'notification_id': notification_id, 'user_id': user_id})

        if serializer.is_valid():
            notification_user = get_object_or_404(NotificationUser, notification_id=notification_id, user_id=user_id)
            try:
                send_push_notification(
                    token=notification_user.user.user_fcmtoken.token,
                    title=notification_user.notification.title,
                    message=notification_user.notification.message
                )
            except Exception as e:
                return Response({"error": "Notification not sent", "details": str(e)})

            notification_user.is_sent = True
            notification_user.sent_time = timezone.now()
            notification_user.save()
            return Response({"status": "Notification sent successfully"})
        else:
            return Response(serializer.errors)
