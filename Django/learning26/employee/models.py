from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.IntegerField()
    join_date = models.DateField(auto_now_add=True)
    post = models.CharField(max_length=100)

    class Meta:
        db_table = "Employee"
        
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    fee = models.IntegerField()
    duration = models.IntegerField()

    class Meta:
        db_table = "course"

    def __str__(self):
        return self.name

class Department(models.Model):
    dept_name = models.CharField(max_length=100)
    dept_location = models.CharField(max_length=100)
    dept_head = models.CharField(max_length=100)

    class Meta:
        db_table = "Department"

    def __str__(self):
        return self.dept_name

class EmployeeSkill(models.Model):
    skill_name = models.CharField(max_length=100)
    skill_level = models.CharField(max_length=50)   # Beginner / Intermediate / Expert
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "EmployeeSkill"

    def __str__(self):
        return self.skill_name