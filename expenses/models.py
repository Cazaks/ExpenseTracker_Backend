from django.conf import settings
from django.db import models

class Category(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=200)
    color = models.CharField(max_length=10, blank=True)
    is_deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.category_name

# Create your models here.
