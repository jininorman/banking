from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def index(request):
   return render(request,"index.html")


def register(request):
   if request.method == 'POST':
      username = request.POST['name']
      password = request.POST['password']
      cpassword = request.POST['cpassword']
      if password == cpassword:
         if User.objects.filter(username=username).exists():
            messages.info(request, 'username already taken')
            return redirect('/')
         else:
            user = User.objects.create_user(username=username, password=password)
            user.save()

      else:
         messages.info(request, "password not matching")
         return redirect('/')
      return redirect('login')
   return render(request, "register.html")


def login(request):
   if request.method == 'POST':
         username = request.POST['name']
         password = request.POST['password']
         user = auth.authenticate(username=username, password=password)
         if user is not None:
            auth.login(request, user)
            return redirect('button')
         else:
            messages.info(request, "Invalid credential")
            return redirect('login')

   return render(request, "login.html")


def button(request):
   return render(request, "button.html")


def form(request):

   return render(request,"application.html")

def open(request):
   return render(request, "open.html")

