from django.urls import path
from . import views
urlpatterns = [
    path('sendemail/', views.sent_email,name="emailsend"),
    path('exportcsv/', views.export_csv,name="exportcsv"),

]
