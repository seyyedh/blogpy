from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from ckeditor.fields import RichTextField
import os
from django.core.exceptions import ValidationError
from django.utils.timezone import now

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extension = ['.jpg','.png','jpeg']

    if not ext.lower() in valid_extension:
        raise ValidationError('Unsupported file extension.')

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='files/user_avatar/',null=False,blank=False,validators=[validate_file_extension])
    description = models.CharField(max_length=512,null=False,blank=False)

class Article(models.Model):
    title = models.CharField(max_length=128,null=False,blank=False)
    cover = models.FileField(upload_to='files/avatar_cover/',null=False,blank=False,validators=[validate_file_extension])
    content = RichTextField()
    created_at = models.DateTimeField(default=now,blank=False)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    promote = models.BooleanField(default=False)

class Category(models.Model):
    title = models.CharField(max_length=128,null=False,blank=False)
    cover = models.FileField(upload_to='files/category_avatar/',null=False,blank=False,validators=[validate_file_extension])

    def __str__(self):
        return self.title