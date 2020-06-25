from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib import messages
from django.views.generic import TemplateView
from .models import project
# Create your views here.

def Homepage(request):
    pros= project.objects.all()
    return render(request,'index.html',{'pros':pros})

