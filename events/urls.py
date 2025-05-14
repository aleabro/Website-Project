from django.urls import path
from . import views

app_name = "events"
urlpatterns = [
    path('details/<int:pk>/', views.DetailView.as_view(), name='details'),
    path('new/', views.EventCreateView.as_view(), name='event_create'),
    path('<int:pk>/update/', views.EventUpdateView.as_view(), name='event_update'),
    path('<int:pk>/delete/', views.EventDeleteView.as_view(), name='event_confirm_delete'),
    path('my_events/', views.OrganizationDashboardView.as_view(), name='organization_dashboard'),

    path('favorite/<int:event_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('unfavorite/<int:event_id>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('favorites/', views.FavoriteListView.as_view(), name='favorite_list'),
]