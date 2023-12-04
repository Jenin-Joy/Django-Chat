from django.urls import path,include
from ChatApp import views 

app_name = "webchat"
urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    # path('ajaxphoto/',views.ajaxphoto,name="ajaxphoto"),
]