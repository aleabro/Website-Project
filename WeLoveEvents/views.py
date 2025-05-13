from django.shortcuts import render
from .models import Event, Organization, User
from django.shortcuts import get_object_or_404
from django.views import generic


# Create your views here.

class IndexView(generic.ListView):
    template_name = "WeLoveEvents/index.html"
    context_object_name = "events"

    def get_queryset(self):
        """
        Return all events.
        """
        return Event.objects.all()

def index(request):
    events = Event.objects.all()
    partners = Organization.objects.all()
    return render(request, 'WeLoveEvents/index.html', {'events': events, 'partners': partners})

def event(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'WeLoveEvents/event.html', {'event': event})
