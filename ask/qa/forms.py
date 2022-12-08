from django import forms
from datetime import datetime
from qa.models import Question, Answer, QuestionManager

class AskForm(forms.Form):
    title = forms.CharField(max_length=255, widget=forms.Textarea)
    text = forms.CharField(widget=forms.Textarea)
    
    def clean_title(self):
        title_field = self.cleaned_data['title']
        if not is_ethic(title_field):
            raise forms.ValidationError('Field contains obscene language')
        return title_field

    def save(self):
        ask = Question(**self.cleaned_data)
        ask.added_at = datetime.now()
        print(ask.added_at)
        ask.save()
        return ask
        
    # class Meta:
    #     model = Question
    #     fields = ['title', 'text']

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.ModelChoiceField(queryset=Question.objects.all(), empty_label=None, widget=forms.Select)
    
    def clean_text(self):
        text_field = self.cleaned_data['text']
        if not is_ethic(text_field):
            raise forms.ValidationError('Field contains obscene language')
        return text_field

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.added_at = datetime.now()
        answer.save()
        return answer

    # class Meta:
    #     model = Answer
    #     fields = ['text']

def is_ethic(field):
    words = ['kaka', 'poh']
    for word in words:
        if word in field:
            return False
    return True