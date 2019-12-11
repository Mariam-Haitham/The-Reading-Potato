from django.db import models
from django.contrib.auth.models import User

from datetime import datetime


class Article(models.Model):
    owner = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    content = models.TextField()
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title