from django.contrib import admin
from .models import Resource, Mentor, Story, ContactMessage

admin.site.register(Resource)
admin.site.register(Mentor)
admin.site.register(Story)
admin.site.register(ContactMessage)
