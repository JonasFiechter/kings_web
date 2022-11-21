from django.shortcuts import render

# Create your views here.

def profiles_login_view(request):
    return render(request, 'profiles/login.html')

def profiles_sign_up_view(request):
    return render(request, 'profiles/sign_up.html')