from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from students.views import journals, groups, students, exams


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
    
    # Exam urls
    path('exam/',
         exams.exams_list,
         name='exam'),
    path('exam/add/',
        exams.exams_add,
        name='exam_add'),
    path('exam/<int:sid>/edit/',
        exams.exams_edit,
        name='exam_edit'),
    path('exam/<int:sid>/delete/',
        exams.exams_delete,
        name='exam_delete'),
    

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
