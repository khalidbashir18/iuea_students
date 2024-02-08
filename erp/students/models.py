from django.db import models

# Create your models here.

class Staff(models.Model):
    Staff_name = models.CharField(max_length=25)
    Contact = models.CharField(max_length=25)
    GENDER_CHOICES =[
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    Gender = models.CharField(choices=GENDER_CHOICES, default='Male', max_length=25)
    Data_Employee = models.DateField(auto_now=True)

class Department(models.Model):
    Dept_name = models.CharField(max_length=25)
    Staff = models.ForeignKey(Staff,on_delete = models.CASCADE)

class Courses(models.Model):
    Courses_name = models.CharField(max_length=10)
    Courses_code = models.CharField(max_length=10)
    Dept_name = models.ForeignKey(Department,on_delete=models.CASCADE)

class Course_unit(models.Model):
    Unit_name = models.CharField(max_length=25)
    Unit_code = models.CharField(max_length=20)
    Course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    Staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
class Student(models.Model):
    Name = models.CharField(max_length=25)
    Student_RegNo = models.CharField(max_length=25, unique=True)
    Student_Email = models.EmailField(max_length=25)
    Studen_Phone = models.CharField(max_length=25)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    Courses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    Reg_Date = models.DateField()