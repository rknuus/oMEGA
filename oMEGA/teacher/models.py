from django.db import models


class Exam(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

    class Admin:
        pass
