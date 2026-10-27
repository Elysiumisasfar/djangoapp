# blog/models.py
from django.db import models
from datetime import *
from django.utils import timezone
from django.utils.timezone import now, localtime
from django.urls import reverse # new
#from datetime import datetime, timedelta, timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
    'auth.User',
    on_delete=models.CASCADE,
    )
    body = models.TextField(default="Enter Text Here")
    

    created_date = timezone.localtime(timezone.now()) 
    published_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title

    def get_absolute_url(self): # new
        return reverse('post_detail', args=[str(self.id)]) 