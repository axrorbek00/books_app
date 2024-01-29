from .models import BookModel, CategoryModel
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save


# @receiver(post_save, sender=CategoryModel)
# def set_count(sender, instance, *args, **kwargs):
#     if instance.category:
#         print('ishladi')
#         cat = CategoryModel.objects.get(name=instance.category)
#         cat.count = cat.books.count()
#         print(cat.count)
#         cat.save()


@receiver(pre_save, sender=BookModel)
def get_real_price(sender, instance, *args, **kwargs):
    if instance.is_discount:
        instance.real_price = ((100 - instance.discount) / 100) * instance.price
    else:
        instance.real_price = instance.price

    # return instance
