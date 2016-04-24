from django.shortcuts import render_to_response
from rest_framework import viewsets

from django.contrib.auth.models import User
from head.serializers import UserSerializer


def index(request):
    return render_to_response('index.html')


def react(request):
    return render_to_response('react.html')


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
