from django.db import models

class Exam(models.Model):
    """Exam Model"""

    subject = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Экзамен"
    )
    date_exam = models.DateField(
        blank=False,
        verbose_name="Дaта экзамена",
        null=True
    )
    teacher = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Имя преподавателя"
    )
    exam_group = models.ForeignKey(
        'Group',
        verbose_name="Группа",
        blank=False,
        on_delete=models.PROTECT
    )
    class Meta:
        verbose_name = "Экзамен"
        verbose_name_plural = "Экзамены"
        
    def __str__(self):
        """ Return name subject of exam and group """
        
        exam_name = '%s %s' % (self.subject, self.exam_group)
        return exam_name.strip()
    