from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAdminUser
from django.core.mail import EmailMessage

from django.conf import settings
from .models import Article
from .serializers import ArticleSerializer, UserSerializer
from rest_framework import mixins, generics


class ListCreateArticle(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, req, *args, **kwargs):
        return self.list(req, *args, **kwargs)

    def post(self, req, *args, **kwargs):
        email = EmailMessage(
            "Hello",
            "Body goes here",
            settings.DEFAULT_FROM_EMAIL,
            [req.user.email],
        )
        email.send()

        return self.create(req, *args, **kwargs)


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ListUser(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateUser(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer
