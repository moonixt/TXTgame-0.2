from django.shortcuts import render
from django.shortcuts import redirect
from .models import User

# Create your views here.

def home(request):
    return render(request,'intro/home.html')

def register(request):
    return render(request,'intro/register.html')

def login(request): # A pagina register primeiro tem a funcionalidade e depois renderiza
    new_user = User()
    new_user.username = request.POST.get('username')
    new_user.password = request.POST.get('password')
    new_user.save()
    return render(request,'intro/data.html')


   