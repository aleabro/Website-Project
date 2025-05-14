from django.contrib import admin
from .models import Event, Favorite
# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'organizer', 'location', 'date', 'is_upcoming')
    list_filter = ('date', 'location')
    search_fields = ('title', 'description', 'location')
    ordering = ('-date',)

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'event')
    list_filter = ('user', 'event')
    search_fields = ('user__username', 'event__title')
    ordering = ('-user',)