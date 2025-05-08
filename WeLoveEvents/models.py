from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    email = models.EmailField()
    password = models.CharField(max_length=200)
    address = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    date_start = models.DateField()
    date_end = models.DateField(blank=True, null=True)
    time_start = models.TimeField()
    time_end = models.TimeField(blank=True, null=True)
    location = models.CharField(max_length=200)
    description = models.TextField()
    poster = models.ImageField()
    organization = models.ManyToManyField(Organization, related_name='events')
    favourite = models.ManyToManyField(User, related_name='favourite_events')

    def __str__(self):
        return self.name


