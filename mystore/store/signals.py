from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver

from .models import Products, Feedbacks


@receiver(post_save, sender=Products)
def create_rating(sender, instance, created, **kwargs):
    if created:
        Feedbacks.objects.create(products=instance)
