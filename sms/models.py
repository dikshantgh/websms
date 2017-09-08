from django.db import models
import django
#from autoslug import AutoSlugField

# Create your models here.

class Group(models.Model):

	name = models.CharField(max_length=20, blank=True)
	number = models.CharField(validators=[django.core.validators.validate_comma_separated_integer_list], blank= True,max_length=200)
	#slug = AutoSlugField(populate_from='name', blank = True)
	
	def __str__(self):
		return self.name


class Message(models.Model):
	
	message = models.TextField(max_length=120, blank = True )
	receiver = models.CharField(validators=[django.core.validators.validate_comma_separated_integer_list], blank= True,max_length=200)
	date = models.DateTimeField(default= django.utils.timezone.now)
	#slug = AutoSlugField(populate_from='message', blank = True)

	
	def __str__(self):
		return self.message

class File(models.Model):
	
	file = models.FileField(upload_to='',blank=True)
	#slug = AutoSlugField(populate_from='file', blank = True)


	def filename(self):
		
		return os.path.basename(self.file.name)
