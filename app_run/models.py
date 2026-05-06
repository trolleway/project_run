from django.db import models
from django.conf import settings

# Create your models here.

class Run(models.Model):
    athlete = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
