from django.shortcuts import render

from events.models import Event

def home_view(request):
    events = Event.objects.all().order_by('-created_at')
    latest_events = events[:3]  # Get the latest 3 events
    return render(request, 'homepage/home.html', {'events': events})