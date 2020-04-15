from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=30)
    done = models.BooleanField(default=False)
