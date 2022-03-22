
from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from resumeBuilder import views

urlpatterns = [
   path('',views.welcomeHome,name='home'),
   path('contactUs/',views.contactUs),
   path('socialNetwork/',views.social),
   path('templates/',views.templte),
   path('Registration/',views.temp,name='signup'),
   path('login/',views.login,name='login'),
   path('Logout/',views.Logout,name='handlelogout'),
   path('ResumeTemplates/',views.ResumeTemplates),
   path('format',views.format,name='format')

   
]
