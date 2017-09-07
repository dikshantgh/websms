from django.contrib import admin
from sms.models import Message,Group, File

# Register your models here.

admin.site.register(Group)
admin.site.register(Message)
admin.site.register(File)