from django import forms
import csv
import re
from sms.models import Message,Group,File



class MessageSendForm(forms.ModelForm):

	receiver = forms.RegexField(regex=r'^([9]\d{9},)*[9]\d{9}$',required = True,help_text="enter single number or numbers separated by comma" )

	def clean(self):
	
		numbers = self.data.get('receiver')
		msg = self.cleaned_data['message']
		number_list = numbers.split(',')
		pattern = re.compile("^([9]\d{9},)*[9]\d{9}$")
		#pattern.match(numbers)
		if pattern.match(numbers):			
		 	for num in number_list:
		 		msg_obj = Message(message=msg, receiver=num)
		 		msg_obj.save()
		
	# # 	#Message.objects.get('').delete()
	# 	#(Message.objects.all()[Message.objects.count()-1]).delete()
		return self.cleaned_data

	class Meta:
		model = Message
		fields = ['message','receiver']
	

class GroupForm(forms.ModelForm):

	name = forms.CharField(required = True)
	number = forms.RegexField(regex=r'^([9]\d{9},)*[9]\d{9}$',required = True )

	#choices = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
	class Meta:
		model = Group
		fields = ['name','number']



class FileForm(forms.ModelForm):

	def validate_file_extension(value):
	
		if not value.name.endswith('.csv'):
			raise forms.ValidationError("")
	
	file = forms.FileField(widget=forms.FileInput(attrs={'accept': ".csv"}),validators=[validate_file_extension])

	class Meta:
		model = File
		fields = ('file',)

	