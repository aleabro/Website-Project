from django.urls import path
from . import views

app_name = "events"
urlpatterns = [
    path('details/<int:pk>/', views.DetailView.as_view(), name='details'),
    path('create/', views.create_event, name='create_event'),
]