from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from .models import UserModel


@receiver(pre_save, sender=UserModel)
def profile_id(sender, instance, *args, **kwargs):
    objects = UserModel.objects.all()
    if objects:
        last_user = objects.last()
        p_id = last_user.profile_id  # A1
        number = int(p_id[1:])  # 1
        number += 1  # 1 + 1 = 2
        p_id = p_id[0] + str(number)  # A2
        instance.profile_id = p_id
    else:
        instance.profile_id = 'A1'
