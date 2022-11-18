from django.shortcuts import render

# Create your views here.

def profiles_login_view(request):
    return render(request, 'profiles/login.html')