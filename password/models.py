from django.db import models

# Create your models here.


class passwords(models.Model):
    username = models.CharField(max_length=16)
    ste = models.CharField(max_length=150, default='hi')
    password = models.CharField(max_length=16, default=None)
    logo = models.CharField(
        max_length=500, default='https://images.unsplash.com/photo-1603366615917-1fa6dad5c4fa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80')
