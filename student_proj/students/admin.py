from django.contrib import admin
from .models.student import Student
from .models.group import Group
from .models.exam import Exam


# Register your models here.
# Регистрация моделей в админ панеле
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Exam)

