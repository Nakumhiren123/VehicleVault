from django.db import models

# Create your models here.
#python class

#parent class Model
#create table student(studentName varchar(100),studentAge int,studentCity varchar(40))
#it will generate pk automatically
class Student(models.Model):
    studentName= models.CharField(max_length=100)
    studentAge = models.IntegerField()
    studentCity = models.CharField(max_length=40)
    studentEmail = models.EmailField(null=True)

    #meta class
    class Meta:
        db_table = "student" #table name

    def __str__(self):
        return self.studentName    


class Product(models.Model):
    productName = models.CharField(max_length=100)
    productPrice = models.IntegerField()
    productDescription = models.TextField()
    productStock = models.PositiveIntegerField()
    productColor = models.CharField(max_length=20,null=True)
    productStatus = models.BooleanField(default=True)
    
    class Meta:
        db_table = "product"

class Customer(models.Model):
    customerName = models.CharField(max_length=100)
    customerEmail = models.EmailField(unique=True)
    customerPhone = models.CharField(max_length=15)
    customerAddress = models.TextField()
    customerStatus = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
       db_table = "customer"


class StudentProfile(models.Model):
    hobbies =(("reading","reading"),("travel","travel"),("music","music"))
    #studentPrilfe id --> pk create auto...
    studentId = models.OneToOneField(Student,on_delete=models.CASCADE)
    studentHobbies = models.CharField(max_length=100,choices=hobbies)
    studentAddress = models.CharField(max_length=100)
    studentPhone = models.CharField(max_length=10)
    studentGender = models.CharField(max_length=10)
    studentDOB = models.DateField()
    
    class Meta:
        db_table = "studentprofile"

    def __str__(self):
        return self.studentId.studentName   


class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    categoryDescription = models.TextField()
    categoryStatus = models.BooleanField(default=True)
    
    class Meta:
        db_table = "category"

    def __str__(self):
        return self.categoryName   

class Service(models.Model):
    serviceName = models.CharField(max_length=100)
    serviceDescription = models.TextField()
    servicePrice = models.IntegerField()
    serviceStatus = models.BooleanField(default=True)
    #after table creation adding new field
    discount = models.IntegerField(null=True)
    categoryId = models.ForeignKey(Category,on_delete=models.CASCADE)

    
    class Meta:
        db_table = "service"

    def __str__(self):
        return self.serviceName    

# take of 06-02-2026
class Company(models.Model):
    companyName = models.CharField(max_length=100)
    companyEmail = models.EmailField()
    companyLocation = models.CharField(max_length=100)
    companyActive = models.BooleanField(default=True)

    class Meta:
        db_table = "company"

    def __str__(self):
        return self.companyName

class CompanyProfile(models.Model):
    company = models.OneToOneField(Company, on_delete=models.CASCADE)
    companyGST = models.CharField(max_length=50)
    companyFounded = models.DateField()
    companyWebsite = models.URLField()
    companyPhone = models.CharField(max_length=15)

    class Meta:
        db_table = "company_profile"

    def __str__(self):
        return self.company.companyName


class Department(models.Model):
    deptName = models.CharField(max_length=100)
    deptHead = models.CharField(max_length=100)
    deptBudget = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        db_table = "department"

    def __str__(self):
        return self.deptName

class Employee(models.Model):
    empName = models.CharField(max_length=100)
    empEmail = models.EmailField()
    empSalary = models.IntegerField()
    empJoinDate = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        db_table = "employee"

    def __str__(self):
        return self.empName


class Project(models.Model):
    projectName = models.CharField(max_length=100)
    projectDescription = models.TextField()
    projectStart = models.DateField()
    projectStatus = models.BooleanField(default=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        db_table = "project"

    def __str__(self):
        return self.projectName

class Task(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDetails = models.TextField()
    taskDeadline = models.DateField()
    taskCompleted = models.BooleanField(default=False)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    class Meta:
        db_table = "task"

    def __str__(self):
        return self.taskTitle