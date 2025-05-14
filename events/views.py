from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Event, Favorite
from .forms import EventForm
from django.views import generic


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

# Mixin to check if the user is an organization
class OrganizationRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.user_type == 'organization'

    def handle_no_permission(self):
        #TODO: handle the case when the user is not authenticated
        messages.error(self.request, "You do not have permission to access this page.")
        if self.request.user.is_authenticated:
            return redirect('/') # Or some other appropriate page
        return redirect('login')


# Mixin to check if the user is a regular user
class RegularUserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.user_type == 'regular'

    def handle_no_permission(self):
        messages.error(self.request, "You do not have permission to access this page.")
        if self.request.user.is_authenticated:
            return redirect('/')
        return redirect('login')

# --- Event CRUD Views for Organizations ---
class EventCreateView(LoginRequiredMixin, OrganizationRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_create.html'
    success_url = reverse_lazy('events:organization_dashboard') # Redirect to org's event list

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        messages.success(self.request, "Event created successfully!")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Create New Event'
        return context

class EventUpdateView(LoginRequiredMixin, OrganizationRequiredMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('events:organization_dashboard')

    def get_queryset(self):
        # Ensure organization can only edit their own events
        return Event.objects.filter(organizer=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "Event updated successfully!")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Update Event'
        return context

class EventDeleteView(LoginRequiredMixin, OrganizationRequiredMixin, DeleteView):
    model = Event
    template_name = 'events/event_confirm_delete.html'
    success_url = reverse_lazy('events:organization_dashboard')

    def get_queryset(self):
        return Event.objects.filter(organizer=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Event deleted successfully.")
        return super().delete(request, *args, **kwargs)


class OrganizationDashboardView(LoginRequiredMixin, OrganizationRequiredMixin, ListView):
    model = Event
    template_name = 'events/organization_dashboard.html'
    context_object_name = 'events'

    def get_queryset(self):
        # Show only events created by the logged-in organization
        return Event.objects.filter(organizer=self.request.user).order_by('-date')


# --- Favorite Event Views for Regular Users ---
@login_required
def add_to_favorites(request, event_id):
    if not request.user.is_regular_user:
        messages.error(request, "Only regular users can favorite events.")
        return redirect('event_detail', pk=event_id) # Or some other page

    event = get_object_or_404(Event, id=event_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, event=event)

    if created:
        messages.success(request, f"'{event.title}' added to your favorites.")
    else:
        messages.info(request, f"'{event.title}' is already in your favorites.")
    return redirect('event_detail', pk=event_id)

@login_required
def remove_from_favorites(request, event_id):
    if not request.user.is_regular_user:
        messages.error(request, "Action not allowed.")
        return redirect('event_detail', pk=event_id)

    event = get_object_or_404(Event, id=event_id)
    favorite = Favorite.objects.filter(user=request.user, event=event)

    if favorite.exists():
        favorite.delete()
        messages.success(request, f"'{event.title}' removed from your favorites.")
    else:
        messages.info(request, f"'{event.title}' was not in your favorites.")
    return redirect('event_detail', pk=event_id) # Or redirect to favorites list

class FavoriteListView(LoginRequiredMixin, RegularUserRequiredMixin, ListView):
    model = Favorite
    template_name = 'events/favorite_list.html'
    context_object_name = 'favorite_items' # Changed from 'favorites' to avoid conflict if any

    def get_queryset(self):
        # Show only favorites of the logged-in regular user
        return Favorite.objects.filter(user=self.request.user).select_related('event').order_by('-event__date')

