from django.shortcuts import get_object_or_404, render
from .models import Exam


def index(request):
    exams = Exam.objects.all()
    context = {'exams': exams}
    return render(request, 'exams/index.html', context)


def exam(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    return render(request, 'exams/exam.html', {'exam': exam})
