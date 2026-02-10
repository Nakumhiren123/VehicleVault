from django.shortcuts import render
from .models import Employee
# Create your views here.

def employeeList(request):
    employees = Employee.objects.all().values()
    print(employees)
    return render(request, 'employee/employeeList.html',{"employees":employees})

def employeeFilter(request):
    employee = Employee.objects.filter(name = 'Ram').values()
    employee2 = Employee.objects.filter(post = 'Developer').values()
    employee3 = Employee.objects.filter(name = 'ram', post = 'Developer').values()

    employee4 = Employee.objects.filter(age__gt=20).values()
    employee5 = Employee.objects.filter(age__gte=20).values()

    employee6 = Employee.objects.filter(post__exact='Developer').values()
    employee7 = Employee.objects.filter(post__iexact='developer').values()

    employee8 = Employee.objects.filter(name__contains='R').values()
    employee9 = Employee.objects.filter(name__icontains='r').values()

    employee10 = Employee.objects.filter(name__startswith='R').values()
    employee11 = Employee.objects.filter(name__endswith='m').values()
    employee12 = Employee.objects.filter(name__istartswith='R').values()
    employee13 = Employee.objects.filter(name__iendswith='m').values()

    employee14 = Employee.objects.filter(name__in=['Ram','Shyam']).values()

    employee15 = Employee.objects.filter(age__range=[20,30]).values()
    
    employee16 = Employee.objects.order_by('age').values()
    employee17 = Employee.objects.order_by('-age').values()

    employee18 = Employee.objects.order_by('-salary').values()

    print('query 1',employee)
    print('query 2',employee2)
    print('query 3',employee3)
    print('query 4',employee4)
    print('query 5',employee5)
    print('query 6',employee6)
    print('query 7',employee7)
    print('query 8',employee8)
    print('query 9',employee9)
    print('query 10',employee10)
    print('query 11',employee11)
    print('query 12',employee12)
    print('query 13',employee13)
    print('query 14',employee14)
    print('query 15',employee15)
    print('query 16',employee16)
    print('query 17',employee17)
    print('query 18',employee18)
    return render(request,'employee/employeeFilter.html')