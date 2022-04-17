from django.shortcuts import render
from django.http import HttpResponse


# Views for Groups

def groups_list(request):
    students = (
        {'id': 1,
         'first_name': 'Дмитро',
         'last_name': 'Подоба',
         'ticket': 235,
         'group': 'МТМ-25',
         'image': 'img/Podoba.jpg'},
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
    return render(request, 'students/groups_list.html',
                  {'students' : students})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request,gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)