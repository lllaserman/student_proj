from django.contrib import admin
from django.urls import path
# from students import views as stud_views
from students.views import journals, groups, students


urlpatterns = [
    # Students urls
    path('',
         students.students_list,
         name='home'),
    path('students/add/',
         students.students_add,
         name='students_add'),
    path('students/<int:sid>/edit/',
         students.students_edit,
         name='students_edit'),
    path('students/<int:sid>/delete/',
         students.students_delete,
         name='students_delete'),

    # Groups urls
    path('groups/',
         groups.groups_list,
         name='groups'),
    path('groups/add/',
         groups.groups_add,
         name='groups_add'),
    path('groups/<str:gid>/edit/',
         groups.groups_edit,
         name='groups_edit'),
    path('groups/<str:gid>/delete/',
         groups.groups_delete,
         name='groups_delete'),

    #Journal urls

    path('journal/',
         journals.students_add,
         name='journal'),

    path('admin/', admin.site.urls),
]
