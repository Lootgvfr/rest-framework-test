from django.contrib.auth.models import User
from .models import Post
from .serializers import UserSerializer, PostSerializer
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('dt_created')
    serializer_class = PostSerializer
