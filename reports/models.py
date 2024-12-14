from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Reports(models.Model):
    title = models.CharField(max_length=200)
    report_image = models.ImageField(blank=True, null=True, upload_to='images/')
    discription = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    date = models.DateTimeField(auto_now_add=True)
    
    


