from django.test import TestCase
from django.urls import reverse
from empapp.models import Department

# Create your tests here.
class DepartmentTests(TestCase):
    def setUp(self):
        Department.objects.create(name ='Just A Test' )
        
    def test_text_content(self):
        dept = Department.objects.get(id=1) 
        # get = read a single record from the database
        excepted_object_name = f'{dept.name}'
        # print(excepted_object_name)
        self.assertEquals(excepted_object_name,'Just A Test')
    
    def test_post_list_view(self):
        response = self.client.get(reverse('list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'Just A Test')
        self.assertTemplateUsed(response,'emp/list.html')
        
