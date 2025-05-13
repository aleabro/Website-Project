from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "events"
urlpatterns = [
    path('', views.index, name='home'),
    path('event/<int:pk>', views.event, name='event'),
]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)