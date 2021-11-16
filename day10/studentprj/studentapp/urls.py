from django.urls import path
from studentapp import views


urlpatterns = [
    path('list/', views.list,name = 'list'),
    path('about/', views.about,name = 'about'),
    path('createnew/', views.create,name = 'create'),
    
    
]
