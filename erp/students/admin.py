from django.contrib import admin
from . models import Staff,Department,Student,Course_unit,Courses

# Register your models here.
admin.site.register(Staff)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Course_unit)
admin.site.register(Courses)