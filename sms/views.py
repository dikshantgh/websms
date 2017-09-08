from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import tablib
from django.contrib.auth.mixins import LoginRequiredMixin

from django import forms
from django.views.generic.edit import FormMixin
from django.contrib.messages.views import SuccessMessageMixin

from sms.models import Message, Group, File
from sms.forms import MessageSendForm , GroupForm,FileForm
# Create your views here.


class MessageSendView(LoginRequiredMixin,SuccessMessageMixin,CreateView):

    template_name = "sms/main_page.html"
    form_class = MessageSendForm
    success_url = reverse_lazy('sms:main_page')
    success_message = 'Message sent successfully'
     

class SentView(LoginRequiredMixin,ListView):

    model = Message
    template_name = "sms/sent_page.html"
    

class GroupCreateView(LoginRequiredMixin,CreateView):

    template_name = "sms/group_create.html"
    form_class = GroupForm
    success_url = reverse_lazy('sms:group_show_page')


class SmsOptionView(TemplateView):

    template_name = 'sms/sms_option_page.html'


class GroupShowView(LoginRequiredMixin,ListView):

    model = Group
    template_name = "sms/group_show_page.html"
    success_url   = reverse_lazy("sms:main_page")
    

    
class GroupUpdateView(LoginRequiredMixin,UpdateView):

    model = Group
    template_name = "sms/group_create.html"
    form_class = GroupForm
    success_url=reverse_lazy('sms:group_show_page')
    success_message = 'Message sent successfully'


class GroupDeleteView(LoginRequiredMixin,DeleteView):

    model = Group
    template_name = "sms/group_delete.html"
    success_url = reverse_lazy('sms:group_show_page')

    
class FileUploadView(LoginRequiredMixin,CreateView):

    template_name = "sms/file_page.html"
    form_class = FileForm
    success_url = reverse_lazy('sms:file_send_page')
    success_message ="Message sent successfully"

    
    def get_csvfile(self):
        return num
        
    def form_valid(self,form):
        
        csvfile = self.request.FILES['file'].read()
        global num
        #data = tablib.Dataset(csvfile)
        #print(data)
        #print(data.export('csv'))
        num = str(csvfile).replace('\\n','').replace('b','').replace("'",'')
        return super(FileUploadView, self).form_valid(form)

  
class GroupSendView(LoginRequiredMixin,SuccessMessageMixin,CreateView):

    template_name = "sms/group_msg_send.html"
    form_class = MessageSendForm
    success_url = reverse_lazy('sms:group_show_page')
    success_message = 'Message sent successful'
    File.objects.all().delete()

  
    def get_number(self):
        group_number = self.request.GET.getlist('choice')
        number_list = []
        for num in group_number:
            number_list.append((Group.objects.get(id =num).number))
        return number_list

    def get_group(self):
        group_number = self.request.GET.getlist('choice')
        group_list = []
        for num in group_number:
            group_list.append((Group.objects.get(id = num).name))
        return group_list
    
    def get_initial(self):
        initials = super(GroupSendView, self).get_initial()
        group = self.get_number()
        if not group:
            initials['receiver'] = ' '
        else:
            initials['receiver'] = str(group).replace('[','').replace(']','').replace("'",'').replace(' ','')      
        return initials

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['group_show'] = self.get_group()
        return context   
      
    
class FileSendView(LoginRequiredMixin,SuccessMessageMixin,CreateView):

    template_name = "sms/file_send_page.html"
    form_class = MessageSendForm
    success_url = reverse_lazy('sms:file_page')
    success_message = 'Message sent successful'
    

    def get_initial(self):
        initials = super().get_initial()
        file_numbers= FileUploadView.get_csvfile(self)
        initials['receiver'] = file_numbers
        return initials


class MessageDeleteView(LoginRequiredMixin,DeleteView):

    model = Message
    template_name = "sms/msg_delete_page.html"
    success_url = reverse_lazy('sms:sent_page')
