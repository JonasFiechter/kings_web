from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile


#TODO: Finish profile index template add logout button
#TODO: Create a profile form (only for admins)
@login_required(login_url='login')
def profiles_profile_view(request):
    profile = {}
    if Profile.objects.filter(email=request.user.id).exists():
        profile = Profile.objects.get(email=request.user.id)
        
    return render(request, 'profiles/index.html', {'profile': profile})

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
    email = request.POST.get('email')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')
    message = ''

    if request.method == 'POST':
        # checking
        if not email or '@' not in email:
            message = 'Email inválido'
        
        elif password != password2:
            message = 'As senhas devem ser iguais!'
        
        elif len(password) <= 5:
            message = 'A senha deve ter no mínimo 6 caracteres!'

        elif User.objects.filter(username=email).exists():
            message = 'O email inserido já está sendo utilizado!'
    
        else:
            user = User.objects.create_user(email, email, password)
            user.save()
            message = 'Usuário criado com sucesso!'
            return render(request, 'profiles/login.html', {
                                                    'success_message': message
                                                })

    return render(request, 'profiles/sign_up.html', {'message': message})

def profiles_logout_view(request):
    if request.user.is_authenticated:
        auth.logout(request)
    
    return render(request, 'profiles/logout.html')