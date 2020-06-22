from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib import messages
from django.views.generic import TemplateView
# Create your views here.

def Homepage(request):
    return render(request,'index.html')

