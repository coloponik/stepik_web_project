from datetime import datetime, timedelta
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from qa.models import Question, Answer, do_signup
from qa.forms import AskForm, AnswerForm, SignUpForm, LoginForm

def test(request, *args, **kwargs):
    return HttpResponse("OK")

def home(request):
    print(request.COOKIES)
    page_obj = paginator(request)
    return render(request, 'index.html', {'page_obj': page_obj})

def pop(request):
    page_obj = paginator(request)
    return render(request, 'pop.html', {'page_obj': page_obj})

def signup(request):
    error = ''
    signup_form = SignUpForm(request.POST)
    if request.method == 'POST' and signup_form.is_valid():
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = do_signup(username, email, password)
        if user:
            return redirect('home')
        else:
            error = 'User/email exists'
    form = SignUpForm()
    return render(request, 'signup.html', {'form': form, 'error': error})

def auth_login(request):
    error = ''
    login_form = LoginForm(request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            error = 'Incorrect login/password'
    form = LoginForm()
    return render(request, 'login.html', {'form': form, 'error': error})

def auth_logout(request):
    logout(request)
    return redirect('home')

def question(request, id=1):
    question = get_object_or_404(Question, id=id)
    try:
        answers = list(Answer.objects.filter(question_id=id))
    except Answer.DoesNotExist:
        answers = None
    answ_form = AnswerForm(request.POST)
    if request.method == 'POST' and answ_form.is_valid():
        answ_form.save(request.user, id)
        return redirect('question', id=id)
    else:
        form = AnswerForm()
        return render(request, 'question.html', {'que': question, 'answers': answers,
                                                 'form': answ_form})

def ask(request):
    ask_form = AskForm(request.POST)
    if request.method == "POST" and ask_form.is_valid():
        just_created = ask_form.save(request.user)
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