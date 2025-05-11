from django.shortcuts import render
from .models import Event, Organization, User
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    events = Event.objects.all()
    partners = Organization.objects.all()
    return render(request, 'WeLoveEvents/index.html', {'events': events, 'partners': partners})

def event(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'WeLoveEvents/event.html', {'event': event})
