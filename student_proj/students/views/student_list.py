from django.views.generic import ListView

from students.models.student import Student


class StudentList(ListView):
    """ Отоброжение данных с помощью класса ListView"""
    model = Student
    context_object_name = 'students'
    template_name = 'students/student_class_view_template.html'

    def get_context_data(self, **kwargs):
        """ This method adds extra varibles to template"""
        # get original context data from parent class
        context = super().get_context_data(**kwargs)

        # tell template not to show logo on a page
        context['show_logo'] = False

        # return context mapping
        return context

    def get_queryset(self):
        """Order students by last_name."""
        # get original query set
        qs = super().get_queryset()

        # order by last name
        return qs.order_by('last_name')