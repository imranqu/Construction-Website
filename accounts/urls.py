from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('book/',views.book,name='book'),
    path('Register/', views.Register.as_view(),name='Register'),
    path('Login/', auth_views.LoginView.as_view(template_name='Login.html'),name='Login'),
    path('Logout/',auth_views.LogoutView.as_view(),name='Logout'),
    path('Profile_Edit/',views.Profile_Edit.as_view(),name="Profile_Edit"),
    

]
