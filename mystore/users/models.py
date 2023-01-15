from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from mystore.orders.models import DeliveryData

phone_validator = RegexValidator(
    r'\d{3}?-?\d{3}?-?\d{4}', 'Only ten numbers and dashes allowed.')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    deliveryData = models.ForeignKey(DeliveryData, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.user.username} Profile'
