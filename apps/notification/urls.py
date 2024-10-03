
from django.urls import path

from apps.notification.views import RegisterFcmToken, CreateNotification, SendNotification

app_name = 'notification'

urlpatterns = [
    path("RegisterFcmToken/", RegisterFcmToken.as_view(), name="register-fcm-token"),
    path("CreateNotificationView/", CreateNotification.as_view(), name="create-notification"),
    path("SendNotification/<int:notification_id>/user/<int:user_id>/", SendNotification.as_view(), name="send-notification"),
]

