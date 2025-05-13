from django.shortcuts import render
from .models import Event
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
class DetailView(generic.DetailView):
    model = Event
    template_name = "events/detail.html"
    context_object_name = "event"

    #TODO: Implement this method that gets the firt three events in the same location
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_events'] = Event.objects.filter(location=self.object.location).exclude(id=self.object.id)[:3]
        return context


class EventForm(forms.ModelForm):
    class Meta:
        model = Event 
        fields = ['title', 'description', 'image', 'date', 'location']   

@login_required
def create_event(request):
    #TODO: add check to see if the user is a company
    # if not request.user.is_company:  
    #     return redirect('homepage')  

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            return redirect('event_detail', event_id=event.id)  
    else:
        form = EventForm()

    return render(request, 'events/create_event.html', {'form': form})