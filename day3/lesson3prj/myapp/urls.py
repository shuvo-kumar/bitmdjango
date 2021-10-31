from django.urls import path
from myapp import views 

urlpatterns = [
    path('list/', views.list,name='emplist'),
    
]
