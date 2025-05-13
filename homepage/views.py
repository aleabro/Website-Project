from django.shortcuts import render

from events.models import Event

def home_view(request):
    events = Event.objects.all().order_by('-created_at')
    return render(request, 'homepage/home.html', {'events': events})