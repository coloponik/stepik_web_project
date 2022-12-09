from datetime import datetime
from django import forms
from django.contrib.auth.models import User 
from qa.models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(max_length=255, widget=forms.Textarea)
    text = forms.CharField(widget=forms.Textarea)
    
    def clean_title(self):
        title_field = self.cleaned_data['title']
        if not is_ethic(title_field):
            raise forms.ValidationError('Field contains obscene language')
        return title_field

    def save(self, username):
        ask = Question(**self.cleaned_data)
        ask.added_at = datetime.now()
        ask.rating = 0
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
        ask.author = user
        ask.save()
        print('---------------------------------')
        print(ask.author)
        return ask

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    
    def clean_text(self):
        text_field = self.cleaned_data['text']
        if not is_ethic(text_field):
            raise forms.ValidationError('Field contains obscene language')
        return text_field

    def save(self, username, que_id):
        answer = Answer(**self.cleaned_data)
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
        answer.added_at = datetime.now()
        answer.question = Question.objects.get(id=que_id)
        answer.author = user
        answer.save()
        return answer

class SignUpForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

def is_ethic(field):
    words = ['kaka', 'poh']
    for word in words:
        if word in field:
            return False
    return True