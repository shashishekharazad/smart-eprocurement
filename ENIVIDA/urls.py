
from django.contrib import admin
from django.urls import path

from .views import index, login, signup, filetender, activetender, Uindex, about, cancelledtender, recruitment, circular, events, contactus, media, verifyotp

from django.urls import path,include
from . import views

urlpatterns = [
    path('', index, name='home'),
    path('login',login, name='login'),
    path('signup',signup),
    path('filetender',filetender, name = 'file'),
    path('activetender',activetender),
    path('U.index', Uindex, name='Uhome'),
    path('about', about, name = 'about'),
    path('cancelledtender', cancelledtender),
    path('recruitment', recruitment, name= 'rec'),
    path('circular', circular, name='circular'),
    path('events', events, name='events'),
    path('contactus', contactus, name='contactus'),
    path('media', media, name='media'),
    path('verifyotp', verifyotp, name='verifyotp'),

    path("",views.home,name="home"),
     path("send_otp",views.send_otp,name="send otp")
]

