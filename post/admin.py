from django.contrib import admin

# Register your models here.
from .models import Job, Feedback, ContactMessage

admin.site.register(Job)
admin.site.register(ContactMessage)
admin.site.register(Feedback)
