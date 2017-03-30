from django.db import models


class Exams(models.Model):
    title = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

    class Admin:
        pass


class Exam(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    exams = models.ForeignKey(Exams)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

    class Admin:
        pass
