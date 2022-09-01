from django.urls import path
from .views import PersonList

urlpatterns = [
    path('test', PersonList.as_view(), name='test')
]