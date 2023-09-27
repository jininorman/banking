from . import views
from django.urls import path

urlpatterns=[

path("",views.index,name="index"),
path("register",views.register,name='register'),
path("login",views.login,name="login"),
path("button",views.button,name="button"),
path("form",views.form,name='form'),
path("open",views.open,name="open"),
    ]