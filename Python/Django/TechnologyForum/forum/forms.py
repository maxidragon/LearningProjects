from django.forms import ModelForm
from .models import Question, Answer


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        exclude = ('createDate', 'user', 'likes')


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        exclude = ('createDate', 'user', 'question', 'likes')
