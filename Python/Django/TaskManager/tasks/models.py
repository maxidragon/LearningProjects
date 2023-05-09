from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    importance = models.BooleanField(default=False)
    createDate = models.DateField(auto_now_add=True)
    completeDate = models.DateField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} {self.createDate} | {self.user.username}'