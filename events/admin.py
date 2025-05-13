from django.contrib import admin
from .models import Event
# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'organizer', 'location', 'date', 'is_upcoming')
    list_filter = ('date', 'location')
    search_fields = ('title', 'description', 'location')
    ordering = ('-date',)