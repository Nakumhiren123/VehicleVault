from django.shortcuts import render

# Create your views here.
def studentHome(request):
    return render(request,"student/studentHome.html")

def studentDashboard(request):
    student = {"name":"raj","age":23,"city":"Ahmedabad"}
    return render(request,"student/studentDashboard.html",student) 


# Sample student data (NO database)
students = [
    {'id': 1, 'name': 'Rahul', 'course': 'Python', 'email': 'rahul@gmail.com'},
    {'id': 2, 'name': 'Priya', 'course': 'Django', 'email': 'priya@gmail.com'},
    {'id': 3, 'name': 'Amit', 'course': 'Data Science', 'email': 'amit@gmail.com'},
]

# 1. Home Page
def search_student(request):
    result = None

    if request.method == "POST":
        name = request.POST.get('name')

        for s in students:
            if s['name'].lower() == name.lower():
                result = s
                break

    return render(request, 'student/search_student.html', {'result': result})


# 2. Student List
def student_list(request):
    return render(request, 'student/student_list.html', {'students': students})


# 3. Student Detail
def student_detail(request, id):
    student = None
    for s in students:
        if s['id'] == id:
            student = s
            break
    return render(request, 'student/student_detail.html', {'student': student})