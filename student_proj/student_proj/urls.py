from django.contrib import admin
from django.urls import path
from students import views as stud_views



urlpatterns = [
    # Students urls
    path('',
         stud_views.students_list,
         name='home'),
    path('students/add/',
         stud_views.students_add,
         name='students_add'),
    path('students/<int:sid>/edit/',
         stud_views.students_edit,
         name='students_edit'),
    path('students/<int:sid>/delete/',
         stud_views.students_delete,
         name='students_delete'),

    # Groups urls
    path('groups/',
         stud_views.groups_list,
         name='groups'),
    path('groups/add/',
         stud_views.groups_add,
         name='groups_add'),
    path('groups/<int:gid>/edit/',
         stud_views.groups_edit,
         name='groups_edit'),
    path('groups/<int:gid>/delete/',
         stud_views.groups_delete,
         name='groups_delete'),

    path('admin/', admin.site.urls),
]
