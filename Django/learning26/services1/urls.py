from django.urls import path
from . import views

urlpatterns = [
    path('serviceList/',views.serviceList,name="serviceList"),
    # path('employeeFilter/', views.employeeFilter),
    # path('createemployee/',views.createEmployee),
    path('createServicesForm/',views.createServicesForm,name="createServicesForm"),
    # path('createCourse/',views.createCourse),
    # path("createDepartment/", views.createDepartment),
    # path("createEmployeeSkill/", views.createEmployeeSkill),
    path("deleteService/<int:id>",views.deleteService,name="deleteService"),
    # path("filterEmployee/",views.filterEmployee,name='filterEmployee'),
    # path("sortEmployee/<int:id>",views.sortEmployee,name='sortEmployee'),
    path("updateService/<int:id>",views.updateService,name='updateService'),

]