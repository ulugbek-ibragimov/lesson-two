from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from apps.notification.models import UserFCMToken, Notification, NotificationUser
from apps.notification.utils import send_push_notification

@receiver(post_save, sender=Notification)
def create_notification_user_objects(sender, instance, created, **kwargs):
    if created:
        users = instance.users.all()
        NotificationUser.objects.bulk_create([NotificationUser(user=user, notification=instance) for user in users])
    else:
        users = instance.users.all()
        for user in users:
            obj,_ = NotificationUser.objects.get_or_create(user=user, notification=instance)
            obj.user = user
            obj.save()


# @receiver(post_save, sender=NotificationUser)
# def send_notification(sender, instance, created, **kwargs):
#     if created:
#         send_push_notification(token=instance.user.user_fcmtoken.token, title=instance.notification.title, message=instance.notification.message)
#         instance.is_sent = True
#         instance.sent_time = timezone.now()
#         instance.save()

