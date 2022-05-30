from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from students.models.student import Student
from students.models.group import Group


def students_list(request):
    students = Student.objects.all()

    # try to order students list
    order_by = request.GET.get('order_by' , '')
    if order_by in ( 'id','last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()

    # paginate students
    paginator = Paginator(students, 3)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        students = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver
        # last page of results.
        students = paginator.page(paginator.num_pages)

    return render(request, 'students/students_list.html',
                  {'students' : students})

def students_add(request):
    # Если форма была запрошена:

        # Если кнопка Отменить была нажата:

            # Возращаем пользователю до списка студентов

        # Если кнопка Добавить была нажата:

            # Провераяем данные на правильность и собираем ошибки

            # Если данные были введены некоректно:
                # Отдаем шаблон форм вместе с найденными ошибками

            # Если данные были введены коректно:
                # Созадаем и сохраняем студента в базу

                # Возращаем пользователя до списка студентов

    # Если форма не была запущенна:
         # возращаем код начального состояния формы
    # was form posted?
    if request.method == "POST":
        # was form add button clicked?
        if request.POST.get('add_button') is not None:

            # errors collection
            errors = {}
            # validate student data will go here
            data = {'middle_name' : request.POST.get('middle_name'),
                    'notes' : request.POST.get('notes')}

            # validate user input
            first_name = request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = "Имя обязательно"
            else:
                data['first_name'] = first_name

            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = "Фамилия обязательно"
            else:
                data['last_name'] = last_name

            birthday = request.POST.get('birthday', '').strip()
            if not birthday:
                errors['birthday'] = "Дата рождения обязательна"
            else:
                data['birthday'] = birthday

            ticket = request.POST.get('ticket', '').strip()
            if not ticket:
                errors['ticket'] = "Билет обязательна"
            else:
                data['ticket'] = ticket

            student_group = request.POST.get('student_group', '').strip()
            if not student_group:
                errors['student_group'] = "Группа обязательна"
            else:
                data['student_group'] = student_group

            photo = request.FILES.get('photo')
            if photo:
                data['photo'] = photo

            # save student
            if not errors:
                student = Student(**data)
                student.save()

                    # redirect to students list
                return HttpResponseRedirect(reverse('home'))

            else:
                # render form with errors and previous user input
                return render(request, 'students/students_add.html',
                              {'groups': Group.objects.all().order_by('title'),
                              'errors': errors})

        elif request.POST.get('cancel_button') is not None:
            # redirect to home page on cancel button
            return HttpResponseRedirect(reverse('home'))

    else:
        # initial form render
        return render(request, 'students/students_add.html',
                      {'groups' : Group.objects.all().order_by('title')})


    #         if not errors:
    # 
    #             # create student object
    #             student = Student(
    #                 first_name = request.POST['first_name'],
    #                 last_name = request.POST['last_name'],
    #                 middle_name = request.POST.get('middle_name'),
    #                 birthday = request.POST['birthday'],
    #                 ticket = request.POST['ticket'],
    #                 student_group = Group.objects.get(pk=request.POST['student_group']),
    #                 photo = request.FILES.get('photo'),
    #             )
    # 
    #             # save it to datebase
    #             student.save()
    # 
    #             # redirect user to students list
    #             return HttpResponseRedirect(reverse('home'))
    # 
    #         else:
    #             # render form with errors and previous user input
    #             return render(request, 'students/students_add.html',
    #               {'groups' : Group.objects.all().order_by('title'),
    #                'errors' : errors})
    # 


def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
