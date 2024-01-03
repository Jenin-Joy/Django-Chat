from django.urls import path,include
from Guest import views
app_name = "webguest"
urlpatterns = [
    path('userreg/',views.userreg,name="userreg"),
    path('',views.login,name="login"),
    path('forgotpassword/',views.forgotpassword,name="forgotpassword"),
    path('otp/',views.otp,name="otp"),
    path('newpass/',views.newpass,name="newpass"),
]