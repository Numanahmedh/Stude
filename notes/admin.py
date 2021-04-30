from django.contrib import admin
from .models import RequestedNotes, AvailableNotes

admin.site.register(RequestedNotes)
admin.site.register(AvailableNotes)
