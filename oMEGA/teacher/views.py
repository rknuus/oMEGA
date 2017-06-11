from django.shortcuts import get_object_or_404, render
from .models import Exam
import json


def index(request):
    exams = Exam.objects.all()
    context = {'exams': exams}
    return render(request, 'exams/index.html', context)


def exam(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    title = exam.title
    text = exam.content.format(**exam.variables)
    return render(request, 'exams/exam.html', {'title': title, 'text': text})
