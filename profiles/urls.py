from django.urls import path
from .views import profiles_login_view, \
                profiles_sign_up_view, \
                profiles_logout_view

urlpatterns = [
    path('login/', profiles_login_view, name='login'),
    path('sign_up/', profiles_sign_up_view, name='sign_up'),
    path('logout/', profiles_logout_view, name='logout'),
]