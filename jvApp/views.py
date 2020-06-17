from django.shortcuts import render
from rest_framework import viewsets
from jvApp.models import User, WildCard
from jvApp.serializers import UserSerializer, WildCardSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class WildCardView(viewsets.ModelViewSet):
    queryset = WildCard.objects.all()
    serializer_class = WildCardSerializer