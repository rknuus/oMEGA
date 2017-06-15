from django.shortcuts import get_object_or_404, render
from .models import Exam
import json


def index(request):
    exams = Exam.objects.all()
    context = {'exams': exams}
    return render(request, 'exams/index.html', context)


def exam(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    questions = {str(question) for question in exam.question_set.select_related()}
    return render(request, 'exams/exam.html', {'title': exam.title, 'questions': questions})
