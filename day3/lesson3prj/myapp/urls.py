'''
আপের আলাদা myapp.py/url.py পরবর্তীতে lesson3prj>url/py থেকে call করা হয়েছে
'''

from django.urls import path
from myapp import views 

urlpatterns = [
    path('list/', views.list,name='emplist'),
    
]
