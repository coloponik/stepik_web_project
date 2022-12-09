from django.db import models
from django.contrib.auth.models import User 

def do_signup(username, email, password):
    double_acc = User.objects.filter(username=username).exists()
    double_email = User.objects.filter(email=email).exists()
    if not double_acc and not double_email:
        user = User.objects.create_user(username, email, password)
    else:
        user = None
    return user

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
    def popular(self):
        return self.order_by('-rating')

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField()
    rating = models.IntegerField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(User, related_name='user_like_que', null=True)
    objects = QuestionManager()

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
