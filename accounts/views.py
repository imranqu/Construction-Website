from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib import messages
from  .models import form,profile
from django.core.mail import send_mail
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView,UpdateView,View,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from django.contrib.auth import get_user_model
from .forms import Form,ProfileForm
from django.http import HttpResponseRedirect

class Register(CreateView):
    form_class=forms.Signup
    success_url=reverse_lazy('Login')
    template_name='Register.html'
      


def book(request):
    form=Form(request.POST or None)
    if form.is_valid():
        form.save()
        send_mail(
                        'Hie from your Website',
                        'You have a new booking',
                        'djangowolf007@gmail.com',
                        ['imranquadri14@gmail.com'],
                        fail_silently=False
                        )

    context={'form':form}
    return render(request,'book.html',context)



class Profile_Edit(LoginRequiredMixin,TemplateView):
    form = forms.EditProfile
    Profile_form = forms.ProfileForm
    template_name = 'Profile_edit.html'

    
    def get(self,request):
        form =forms.EditProfile(instance=request.user)
        Profile_form=forms.ProfileForm(instance=request.user.profile)
        args={'form':form,'Profile_form':Profile_form}

        return render(request,'Profile_edit.html',args)

    def post(self,request):
        form = forms.EditProfile(request.POST or None ,instance=request.user)
        Profile_form=forms.ProfileForm(request.POST ,instance=request.user.profile)
        if form.is_valid() and Profile_form.is_valid():
            user=form.save()
            Profile_form.save()
            
            return redirect(reverse('Homepage'))
        

