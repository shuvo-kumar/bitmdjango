from django.urls import path
from studentapp import views


urlpatterns = [
    path('list/', views.list,name = 'list'),
    path('about/', views.about,name = 'about'),
    # crud
    path('createnew/', views.create,name = 'create'),
    path('view/<int:id>', views.details,name = 'view'),
    path('edit/<int:id>', views.edit,name = 'edit'),
    path('delete/<int:id>', views.delete,name = 'delete'),
]
