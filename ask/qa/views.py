from django.http import HttpResponse
from qa.models import Question
from django.core.paginator import Paginator
from django.shortcuts import render

def test(request, *args, **kwargs):
    return HttpResponse("OK")

def home(request):
    page_obj = paginator(request)
    return render(request, 'index.html', {'page_obj': page_obj})

def pop(request):
    page_obj = paginator(request)
    return render(request, 'pop.html', {'page_obj': page_obj})

def paginator(request):
    if request.path[1:-1] == 'popular':
        question_list = Question.objects.popular()
    else:
        question_list = Question.objects.new()
    paginator = Paginator(question_list, 3)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    return page