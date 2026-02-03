from django.urls import path
from . import views

urlpatterns = [

    path("home/",views.studentHome),
    path("dashboard/",views.studentDashboard),
    path('search/', views.search_student),
    path('list/', views.student_list, name = "student_list"),
    path('detail/<int:id>/', views.student_detail,name ="student_detail"),
]