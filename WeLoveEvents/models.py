from django.db import models

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

    def __str__(self):
        return self.name