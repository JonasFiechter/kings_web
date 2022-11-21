from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.

def profiles_login_view(request):
    username = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    message = ''

    if user is not None:
        login(request, user)
        #redirect
    if request.method == 'POST' and not user:
        message = 'Usuário ou senha inválidos'

    return render(request, 'profiles/login.html', {'message': message})

def profiles_sign_up_view(request):
    return render(request, 'profiles/sign_up.html')