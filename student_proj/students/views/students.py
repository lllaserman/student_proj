from django.shortcuts import render
from django.http import HttpResponse

#  Views for Students

def students_list(request):
    students = (
        {'id' : 1,
         'first_name' : 'Дмитро',
         'last_name' : 'Подоба',
         'ticket' : 235,
         'group' : 'МТМ-25',
         'image' : 'img/Podoba.jpg'},
        {'id': 2,
         'first_name': 'Максим',
         'last_name': 'Кашпаров',
         'ticket': 234,
         'group': 'МТМ-26',
         'image': 'img/Kashparov.jpg'},
        {'id': 3,
         'first_name': 'Мария',
         'last_name': 'Богак',
         'ticket': 233,
         'group': 'МТМ-27',
         'image': 'img/Bohak.jpg'},
    )
    return render(request, 'students/students_list.html',
                  {'students' : students})

def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
