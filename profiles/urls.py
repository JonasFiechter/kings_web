from django.urls import path
from .views import profiles_auth_view

urlpatterns = [
    path('', profiles_auth_view, name='profiles')
]