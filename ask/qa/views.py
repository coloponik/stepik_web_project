from django.http import HttpResponse
from qa.models import Question
from django.core.paginator import Paginator
from django.shortcuts import render

def test(request, *args, **kwargs):
    return HttpResponse("OK")

def home(request):
    question_list = Question.objects.all()
    page_obj = paginator(request, question_list)
    return render(request, 'index.html', {'page_obj': page_obj, 'que_list': question_list})

def paginator(request, objects):
    paginator = Paginator(objects, 3)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    return page