from django.contrib.auth.models import User
from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    message = models.CharField(max_length=500, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="leads")
    created_at = models.DateTimeField(auto_now_add=True)


