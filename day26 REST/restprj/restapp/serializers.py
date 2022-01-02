from rest_framework import serializers
from restapp.models import EmployeeInfo

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmployeeInfo
        fields = ('id', 'name', 'email')
        
    