import datetime

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class NormalUser(models.Model):
    user = models.OneToOneField(User, null=True)
    nickname = models.CharField(max_length=50, verbose_name = "username")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="joined at")

    def username(self):
        if self.Name:
            return self.nickname
        else:
            return self.user.username

    def __str__(self):
        return self.nickname

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = verbose_name = "User Information"