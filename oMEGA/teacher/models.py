from django.db import models
from jsonfield import JSONField


class Exam(models.Model):
    title = models.CharField(max_length=250)
    variables = JSONField(default={})
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

    class Admin:
        pass
