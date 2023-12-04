from django.shortcuts import render,redirect
from Guest.models import *
from django.db.models import Q
from ChatApp.models import *
from datetime import datetime
# Create your views here.

def homepage(request):
    user = tbl_user.objects.exclude(id=request.session["uid"])
    return render(request,"ChatApp/HomePage.html",{"user":user})

# def ajaxphoto(request):
#     tbl_photo.objects.create(photo=request.FILES.get("file"))
#     return render(request,"ChatApp/NewPage.html")

def chatpage(request,id):
    user  = tbl_user.objects.get(id=id)
    return render(request,"ChatApp/Chat.html",{"user":user})

def ajaxchat(request):
    file = request.FILES.get("file")
    if file != '':
        if request.POST.get("msg") != '':
            from_user = tbl_user.objects.get(id=request.session["uid"])
            to_user = tbl_user.objects.get(id=request.POST.get("tid"))
            tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user_from=from_user,user_to=to_user,chat_file=request.FILES.get("file"))
            return render(request,"ChatApp/Chat.html")
        else:
            from_user = tbl_user.objects.get(id=request.session["uid"])
            to_user = tbl_user.objects.get(id=request.POST.get("tid"))
            tbl_chat.objects.create(chat_content="",chat_time=datetime.now(),user_from=from_user,user_to=to_user,chat_file=request.FILES.get("file"))
            return render(request,"ChatApp/Chat.html")
    else:
        from_user = tbl_user.objects.get(id=request.session["uid"])
        to_user = tbl_user.objects.get(id=request.POST.get("tid"))
        tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user_from=from_user,user_to=to_user,chat_file="")
        return render(request,"ChatApp/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_user.objects.get(id=request.session["uid"])
    chat_data = tbl_chat.objects.filter((Q(user_from=user) | Q(user_to=user)) & (Q(user_from=tid) | Q(user_to=tid))).order_by('chat_time')
    return render(request,"ChatApp/ChatView.html",{"data":chat_data,"tid":int(tid)})