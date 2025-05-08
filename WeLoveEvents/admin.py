from django.contrib import admin
from .models import Event
from .models import Organization
from .models import User

# Register your models here.
admin.site.register(Event)
admin.site.register(Organization)
admin.site.register(User)