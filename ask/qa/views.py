from django.http import HttpResponse
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

def test(request, *args, **kwargs):
    return HttpResponse("OK")

def home(request):
    page_obj = paginator(request)
    return render(request, 'index.html', {'page_obj': page_obj})

def pop(request):
    page_obj = paginator(request)
    return render(request, 'pop.html', {'page_obj': page_obj})

def question(request, id=1):
    question = get_object_or_404(Question, id=id)
    try:
        answers = list(Answer.objects.filter(question_id=id))
    except Answer.DoesNotExist:
        answers = None
    answ_form = AnswerForm(request.POST)
    if request.method == 'POST' and answ_form.is_valid():
        answ_form.save()
        return redirect('question', id=id)
    else:
        form = AnswerForm()
        return render(request, 'question.html', {'que': question, 'answers': answers, 'form': answ_form})

def ask(request):
    ask_form = AskForm(request.POST)
    if request.method == "POST" and ask_form.is_valid():
        just_created = ask_form.save()
        return redirect('question', id=just_created.id)
    else:
        form = AskForm()
        return render(request, 'ask.html', {'form': form})

def paginator(request):
    if request.path[1:-1] == 'popular':
        question_list = Question.objects.popular()
    else:
        question_list = Question.objects.new()
    paginator = Paginator(question_list, 3)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    return page