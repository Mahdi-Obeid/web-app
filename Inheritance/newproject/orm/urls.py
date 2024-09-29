from django.urls import path
from .views import createApp

urlpatterns = [
    path('', createApp, name='createApp'),
]
