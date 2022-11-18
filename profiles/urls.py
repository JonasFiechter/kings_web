from django.urls import path
from .views import profiles_login_view

urlpatterns = [
    path('login/', profiles_login_view, name='profiles')
]