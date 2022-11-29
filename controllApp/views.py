from django.shortcuts import render

# Create your views here.
from .serializers import DataSerialize
from .models import *
from django.views.decorators.http import require_http_methods
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view

from controllApp import serializers


@api_view(['GET'])
def allUser(request):
    data = User.objects.get()
    serialize = DataSerialize(data,many =False)
    
    return Response(serialize.data)
