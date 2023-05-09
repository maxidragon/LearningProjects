from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuestionForm, AnswerForm
from .models import Question, Answer


def home(req):
    return render(req, 'index.html')


@login_required
def create(req):
    if req.method == 'POST':
        form = QuestionForm(req.POST, req.FILES)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = req.user
            question.save()
            return redirect('forum:home')
        else:
            error = "Something is wrong. Try again!"
            return render(req, 'create.html', {'error': error, 'categories': Question.CATEGORY_CHOICES})
    else:
        return render(req, 'create.html', {'categories': Question.CATEGORY_CHOICES})


@login_required
def questions(req):
    category = req.GET.get('category')
    if category:
        questionsList = Question.objects.filter(category=category).order_by('-createDate')
        return render(req, 'questions.html',
                      {'questions': questionsList, 'categories': Question.CATEGORY_CHOICES, 'category': category})
    questionsList = Question.objects.all().order_by('-createDate')
    return render(req, 'questions.html', {'questions': questionsList, 'categories': Question.CATEGORY_CHOICES})


@login_required
def myQuestions(req):
    questionsList = Question.objects.filter(user=req.user).order_by('-createDate')
    return render(req, 'myquestions.html', {'questions': questionsList})


@login_required
def detail(req, questionId):
    question = get_object_or_404(Question, pk=questionId)
    likes = question.likes.all()
    liked = False
    if req.user in likes:
        liked = True
    return render(req, 'detail.html', {'question': question, 'answers': question.answers.all(), 'liked': liked})


@login_required
def like(req, questionId):
    question = get_object_or_404(Question, pk=questionId)
    likes = question.likes.all()
    if req.method == 'POST':
        liked = False
        if req.user in likes:
            liked = True
        if liked:
            question.likes.remove(req.user)
        else:
            question.likes.add(req.user)
        return redirect('forum:detail', questionId)
    else:
        likes = question.likes.all()
        liked = False
        if req.user in likes:
            liked = True
        return render(req, 'detail.html', {'question': question, 'answers': question.answers.all(), 'liked': liked})


@login_required
def likeAnswer(req, answerId):
    answer = get_object_or_404(Answer, pk=answerId)
    question = answer.question
    likes = answer.likes.all()
    if req.method == 'POST':
        liked = False
        if req.user in likes:
            liked = True
        if liked:
            answer.likes.remove(req.user)
        else:
            answer.likes.add(req.user)
        return redirect('forum:detail', question.id)
    else:
        likes = question.likes.all()
        liked = False
        if req.user in likes:
            liked = True
        return render(req, 'detail.html', {'question': question, 'answers': question.answers.all(), 'liked': liked})


@login_required
def edit(req, questionId):
    question = get_object_or_404(Question, pk=questionId)
    if question.user == req.user:
        if req.method == 'POST':
            form = QuestionForm(req.POST, req.FILES, instance=question)
            if form.is_valid():
                form.save()
                return render(req, 'detail.html', {'question': question, 'answers': question.answers.all()})
            else:
                error = "Something is wrong. Try again!"
                return render(req, 'edit.html', {'question': question, 'error': error})
        else:
            return render(req, 'edit.html', {'question': question, 'categories': Question.CATEGORY_CHOICES})


@login_required
def delete(req, questionId):
    question = get_object_or_404(Question, pk=questionId)
    if question.user == req.user:
        question.delete()
        return redirect('forum:myQuestions')
    else:
        return redirect('forum:home')


@login_required
def addAnswer(req):
    if req.method == 'POST':
        form = AnswerForm(req.POST, req.FILES)
        question = get_object_or_404(Question, pk=req.POST['question'])
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = req.user
            answer.question = question
            answer.save()
            return render(req, 'detail.html', {'question': question, 'answers': question.answers.all()})
        else:
            error = "Something is wrong. Try again!"
            return render(req, 'detail.html', {'question': question, 'error': error, 'answers': question.answers.all()})
    else:
        return redirect('forum:home')


@login_required
def editAnswer(req, answerId):
    answer = get_object_or_404(Answer, pk=answerId)
    question = get_object_or_404(Question, pk=answer.question.id)
    if req.method == 'POST':
        form = AnswerForm(req.POST, req.FILES, instance=answer)
        if form.is_valid():
            form.save()
            return render(req, 'detail.html', {'question': question, 'answers': question.answers.all()})
        else:
            error = "Something is wrong. Try again!"
            return render(req, 'detail.html', {'question': question, 'error': error, 'answers': question.answers.all()})
    else:
        return render(req, 'editAnswer.html', {'answer': answer})


@login_required
def deleteAnswer(req, answerId):
    answer = get_object_or_404(Answer, pk=answerId)
    if answer.user == req.user:
        answer.delete()
        return redirect('forum:questions')
    else:
        return redirect('forum:home')
