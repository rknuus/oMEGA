from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render
from .models import Exam


def index(request):
    exams = Exam.objects.all()
    template = loader.get_template('exams/index.html')
    context = {'exams': exams}
    return HttpResponse(template.render(context, request))
    # return render(request, 'exams/index.html', context)


def exam(request, exam_id):
    try:
        exam = Exam.objects.get(pk=exam_id)
    except Exam.DoesNotExist:
        raise Http404('Exam does not exist')
    return render(request, 'exams/exam.html', {'exam': exam})
