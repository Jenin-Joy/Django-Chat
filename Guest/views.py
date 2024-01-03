from django.shortcuts import render,redirect
from Guest.models import *
import random
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.

def userreg(request):
    if request.method == "POST":
        tbl_user.objects.create(user_name=request.POST.get("txt_name"),user_contact=request.POST.get("txt_contact"),user_email=request.POST.get("txt_email"),user_password=request.POST.get("txt_password"))
        return render(request,"Guest/NewUser.html")
    else:
        return render(request,"Guest/NewUser.html")   

def login(request):
    if request.method == "POST":
        usercount = tbl_user.objects.filter(user_email=request.POST.get("txt_email"),user_password=request.POST.get("txt_password")).count()
        if usercount > 0:
            user = tbl_user.objects.get(user_email=request.POST.get("txt_email"),user_password=request.POST.get("txt_password"))
            request.session["uid"] = user.id
            request.session["uname"] = user.user_name
            return redirect("webchat:homepage")
        else:
            return render(request,"Guest/Login.html",{"msg":"Invalid Email Or Password"})
    else:
        return render(request,"Guest/Login.html")

def forgotpassword(request):
    if request.method == "POST":
        email = request.POST.get("txt_email")
        user = tbl_user.objects.get(user_email=email)
        otp = random.randint(111111,999999)
        request.session["otp"] = otp
        request.session["fid"] = user.id
        send_mail(
            'Forgot password OTP', #subject
            "\rHello \r" + str(otp) +"\n This is the OTP to reset ur password.\n If you didn't ask to reset your password, you can ignore this email. \r\n Thanks. \r\n Your D MARKET team.",#body
            settings.EMAIL_HOST_USER,
            [email],
        )
        return render(request,"Guest/ForgotPassword.html",{"msg":email})
    else:
        return render(request,"Guest/ForgotPassword.html")

def otp(request):
    if request.method == "POST":
        inp_otp = int(request.POST.get("txt_otp"))
        if inp_otp == request.session["otp"]:
            return redirect("webguest:newpass")
        else:
            return render(request,"Guest/OTP.html",{"msg":"OTP Does not Matches..!!"})
    else:
        return render(request,"Guest/OTP.html")

def newpass(request):
    if request.method == "POST":
        user = tbl_user.objects.get(id=request.session["fid"])
        if request.POST.get("txt_new_pass") == request.POST.get("txt_con_pass"):
            user.user_password = request.POST.get("txt_con_pass")
            user.save()
            return render(request,"Guest/NewPassword.html",{"msg1":"Password Updated Sucessfully...."})
        else:
            return render(request,"Guest/NewPassword.html",{"msg":"Error in confirm password..!!!"})
    else:
        return render(request,"Guest/NewPassword.html")