from django.db import models
from Guest.models import *
# Create your models here.

class tbl_chat(models.Model):
    chat_content = models.CharField(max_length=500)
    chat_time = models.DateTimeField()
    chat_file = models.FileField(upload_to='ChatFiles/')
    user_from = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_from")
    user_to = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_to")

# class tbl_photo(models.Model):
#     photo = models.FileField(upload_to='ChatFiles/')