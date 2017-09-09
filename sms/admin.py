from django.contrib import admin
from sms.models import Message,Group, File

# Register your models here.

admin.site.register(Group)
admin.site.register(Message)
admin.site.register(File)

# @admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    

	list_display = ('message', 'receiver', 'date','sender')
	



# @admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
	list_display = ('message', 'receiver', 'date','sender')

# @admin.register(File)
# class FileAdmin(admin.ModelAdmin):
