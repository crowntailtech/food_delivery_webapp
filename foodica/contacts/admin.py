from contacts.views import complaint
from contacts.models import Contacts, Feedback, Complaint
from django.contrib import admin

# Register your models here.
admin.site.register(Contacts)
admin.site.register(Feedback)
admin.site.register(Complaint)