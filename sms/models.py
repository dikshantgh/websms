from django.db import models
import django
from django.contrib.auth.models import User

# Create your models here.

class Group(models.Model):

	name = models.CharField(max_length=20, blank=True)
	number = models.CharField(validators=[django.core.validators.validate_comma_separated_integer_list], blank= True,max_length=200)
	sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	
	def __str__(self):
		return self.name


class Message(models.Model):
	
	message = models.TextField(max_length=120, blank = True )
	receiver = models.CharField(validators=[django.core.validators.validate_comma_separated_integer_list], blank= True,max_length=200)
	date = models.DateTimeField(default= django.utils.timezone.now)
	sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


	
	def __str__(self):
		return self.message

class File(models.Model):
	
	file = models.FileField(upload_to='',blank=True)
	sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)



	def filename(self):
		
		return os.path.basename(self.file.name)
