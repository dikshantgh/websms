from django.conf.urls import url
from sms import views


app_name ='sms'
urlpatterns = [


    #url(r"^$", views.HomeView.as_view(), name="home_page"),
    url(r"^$", views.SmsOptionView.as_view(), name="sms_option_page"),
    url(r"^messages/$", views.SentView.as_view(), name="sent_page"),
	url(r"^groupcreate/$", views.GroupCreateView.as_view(), name="group_create"),
	url(r"^messagesend$", views.MessageSendView.as_view(), name="main_page"),
	url(r"^groupshow/$", views.GroupShowView.as_view(), name="group_show_page"),
	url(r"^groupupdate/(?P<pk>\d+)/$", views.GroupUpdateView.as_view(), name="group_update_page"),
	url(r"^groupdelete/(?P<pk>\d+)/$", views.GroupDeleteView.as_view(), name="group_delete_page"),
	url(r"^fileupload/$", views.FileUploadView.as_view(), name="file_page"),
	url(r"^groupsend/(?P<pk>\d+)/$", views.GroupSendView.as_view(), name="group_msg_send"),
	url(r"^msgdelete/(?P<pk>\d+)/$", views.MessageDeleteView.as_view(), name="msg_delete_page"),
	url(r"^filesend/$", views.FileSendView.as_view(), name="file_send_page"),



]
