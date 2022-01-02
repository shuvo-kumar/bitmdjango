from django.shortcuts import render,get_object_or_404
from django.urls.base import reverse_lazy
from django.views.generic import *
from empapp.models import Employee,Department
from empapp.forms import EmployeeForm
from django.contrib import messages
from django.urls import reverse
from django.db.models import Count
from django.db.models import Q



# Create your views here.

class HomeView(TemplateView):
    template_name = 'emp/home.html'
    
class EmployeeListView(ListView):
    model = Employee
    template_name = 'emp/list.html'
    # paginate_by = 10
    queryset = Employee.objects.order_by('-id')
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Employee List"
        return context    
    
class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'emp/empform.html'
    form_class = EmployeeForm
    
    def get_success_url(self)->str:
        messages.add_message(self.request,messages.INFO,'Employee Created Successfully')
        return reverse('list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Employee Entry'
        context["heading" ] = 'Create New Employee'
        return context   
    
class EmployeeDetailView(DetailView):
    queryset = Employee.objects.all()
    template_name = 'emp/details.html' 
    
class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'emp/empform.html'
    form_class = EmployeeForm
    
    def get_success_url(self):
        messages.add_message(self.request, messages.INFO,'Employee Has Been Updated')
        return reverse('list')  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Employee'
        context["heading" ] = 'Update Employee'
        return context  
    
class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'emp/delete1.html'
    form_class = EmployeeForm
    # success_url = reverse_lazy('list')
    def get_success_url(self):
        messages.add_message(self.request, messages.INFO,'Employee Has Been Deleted')
        return reverse('list') 
    
    
def showchart(request, chartType):
    labels =[]
    data =[]
    queryset = Employee.objects.values('department__name').annotate(num_employees= Count('department_id')).all()
    for emp in queryset:
        labels.append(emp['department__name'])
        data.append(emp['num_employees'])
    
    context= {'title' : 'Chart', 'labels' : labels, 'data' : data, 'chartType': chartType }
    return render(request, 'emp/chart.html',context)
        
def show(request, departmentname = None):
    departments = None
    employees = None
    
    
    if departmentname != None:
        departments = get_object_or_404(Department,name=departmentname)
        employees = Employee.objects.filter(department=departments)
        page_employees = employees
        emp_count = employees.count()
    
    else:
        employees = Employee.objects.all().order_by('id')
        page_employees = employees
        emp_count = employees.count()
        
    context = {
        'object_list':page_employees,
        'emp_count': emp_count,
    }
    return render(request, 'emp/list.html', context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            employees=Employee.objects.order_by('-name').filter(Q(name__contains=keyword)| 
                                                                Q(email__contains=keyword)|
                                                                Q(salary__contains=keyword) |
                                                                Q(dob__contains=keyword)
                                                                )
            emp_count = employees.count()
            
    context = {
        'object_list':employees,
        'emp_count': emp_count,
    }
    return render(request, 'emp/list.html', context)
            
        
        
        