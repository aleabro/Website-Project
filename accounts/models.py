from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_company = models.BooleanField(default=False, verbose_name="Azienda")
    is_user = models.BooleanField(default=True, verbose_name="Utente")

    def __str__(self):
        return self.username

class CompanyProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='company_profile')
    company_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)

    def __str__(self):
        return self.company_name

