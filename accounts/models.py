from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('regular', 'Regular User'),
        ('organization', 'Organization'),
    )
    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        default='regular',
        help_text="Designates the type of user."
    )
    


    def __str__(self):
        return self.username



