from django.shortcuts import render,HttpResponse,redirect
from .models import Employee,Department, EmployeeSkill
from .forms import EmployeeForm,CourseForm, DepartmentForm, EmployeeSkillForm
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

def createEmployee(request):
    Employee.objects.create(name='ajay',age=23,salary=23000,post='HR',join_date='2022-01-01')
    return HttpResponse('EMPLOYEE CREATED...')

def createEmployeeWithForm(request):
    print(request.method)
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        form.save()
        return HttpResponse("EMPLOYEE CRATED...")

    else:
        form = EmployeeForm()
        return render(request, "employee/createEmployeeForm.html",{"form":form})

def createCourse(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        form.save()
        return HttpResponse("COURSE CREATED")

    else:
        form = CourseForm()
        return render(request, "employee/createCourse.html",{"form":form})

def createDepartment(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        form.save()
        return HttpResponse("DEPARTMENT CREATED")

    else:
        form = DepartmentForm()
        return render(request, "employee/createDepartment.html", {"form": form})

def createEmployeeSkill(request):
    if request.method == 'POST':
        form = EmployeeSkillForm(request.POST)
        form.save()
        return HttpResponse("EMPLOYEE SKILL CREATED")

    else:
        form = EmployeeSkillForm()
        return render(request, "employee/createEmployeeSkill.html", {"form": form})