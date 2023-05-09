from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', blank=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    CATEGORY_CHOICES = [
        ('PY', 'Python'),
        ('JS', 'JavaScript'),
        ('TS', 'TypeScript'),
        ('CS', 'C#'),
    ]
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default='PY')
    likes = models.ManyToManyField('auth.User', related_name='likes', blank=True)

    def __str__(self):
        return f'{self.title} | {self.user.username}'


class Answer(models.Model):
    text = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', blank=True)
    createDate = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    likes = models.ManyToManyField('auth.User', related_name='answerLikes', blank=True)
    def __str__(self):
        return f'{self.question.title} | {self.user.username}'
