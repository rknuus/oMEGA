from django.db import models
from jsonfield import JSONField


class Exam(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

    class Admin:
        pass


class Question(models.Model):
    variables = JSONField(default={})
    content = models.TextField()
    question = models.ForeignKey(Exam, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.content.format(**self.variables)

    class Admin:
        pass
