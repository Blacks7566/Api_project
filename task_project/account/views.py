from django.shortcuts import render
from account.models import User
from account.serializers import RegistrationSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.


class UserApi(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer