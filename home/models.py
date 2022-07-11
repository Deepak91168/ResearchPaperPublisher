from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone
from tinymce.models import HTMLField

class Category(models.Model):
    title = models.CharField(max_length=50)
    cat_id = models.AutoField(primary_key=True)
    description = models.TextField(max_length=1000)
    add_date = models.DateField(auto_now_add=True, null=True)
    add_time = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to="category")
    url = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class Posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = HTMLField()
    post_author = models.CharField(max_length=50, default='NSP')
    post_description = models.TextField(max_length=500, null=True)
    url = models.CharField(max_length=50)
    image = models.ImageField(upload_to="posts")
    file = models.FileField(upload_to="files", null=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    post_date = models.DateField(auto_now_add=True, null=True)
    post_time = models.DateTimeField(auto_now_add=True, null=True)
    
    def time_diff(self):
        timediff = int(timezone() - self.post_time)
        print(timediff.total_seconds())
        return timediff

    def __str__(self):
        return self.title