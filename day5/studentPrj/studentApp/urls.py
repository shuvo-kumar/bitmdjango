from django.urls import path
from studentApp import views

urlpatterns = [
    path('list/', views.list, name='list')
]
