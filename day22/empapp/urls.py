from django.urls import path
from empapp import views

urlpatterns = [
    
    path('list/',views.EmployeeListView.as_view(), name='list'),
    path('create/',views.EmployeeCreateView.as_view(), name='create'),
    path('detail/<int:pk>',views.EmployeeDetailView.as_view(), name='detail'),
    path('edit/<int:pk>',views.EmployeeUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>',views.EmployeeDeleteView.as_view(), name='delete'),
    
]