from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin
from django.conf import settings

# Create your models here.
class Event(models.Model):
    organizer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="events",
        limit_choices_to={'user_type': 'organization'}
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="event_images/")
    #TODO: add a video field
    #video = models.FileField(upload_to="event_videos/", blank=True, null=True)
    date = models.DateTimeField("event date")
    location = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def was_published_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)
    

    def __str__(self):
        return self.title

    @admin.display(
        boolean=True,
        ordering="date",
        description="Upcoming?",
    )
    def is_upcoming(self):
        return self.date >= timezone.now()
    
class Favorite(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="favorites"
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="favorites")
    
    class Meta:
        unique_together = ('user', 'event')
    
    def __str__(self):
        return f"{self.user.username} - {self.event.title}"
    
    
    
