from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    text = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return f'{self.title} | {self.date}'