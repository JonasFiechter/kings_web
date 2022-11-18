from django.shortcuts import render

# Create your views here.

def profiles_auth_view(request):
    return render(request, 'profiles/profiles_index.html')