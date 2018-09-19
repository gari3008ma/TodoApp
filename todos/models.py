from __future__ import unicode_literals
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    domain = models.CharField(max_length=200)
    is_approved = models.BooleanField(default=False)
    is_domain_admin = models.BooleanField(default=False)


class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null= True, related_name='created_tasks')
    assigned_to = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null= True, related_name='assigned_tasks')
    status = models.BooleanField(default=False)
    deadline = models.DateTimeField(blank=True,default=datetime.now)
    def __str__(self):
        return self.title


class Domain(models.Model):
    name = models.CharField(max_length=200)
