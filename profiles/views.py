from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import auth


def profiles_login_view(request):
    username = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    message = ''
    
    if request.user.is_authenticated:
        return redirect('home')

    elif user is not None:
        login(request, user)
        return redirect('home')
        
    elif request.method == 'POST' and not user:
        message = 'Usuário ou senha inválidos'

    return render(request, 'profiles/login.html', {'message': message})

def profiles_sign_up_view(request):
    username = request.POST.get('email')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')
    message = ''

    if request.method == 'POST':
        # checking
        if not username:
            message = 'Email inválido'
        
        elif password != password2:
            message = 'As senhas devem ser iguais!'
        
        elif len(password) <= 5:
            message = 'A senha deve ter no mínimo 6 caracteres!'
        
    return render(request, 'profiles/sign_up.html', {'message': message})

def profiles_logout_view(request):
    if request.user.is_authenticated:
        auth.logout(request)
    
    return render(request, 'profiles/logout.html')