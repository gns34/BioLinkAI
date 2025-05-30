from django.urls import path
from . import views

urlpatterns = [
    path('infinity/', views.showinfinity, name='infinityview'),
]
