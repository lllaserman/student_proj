from django.db import models


class Student(models.Model):
    """Student Model"""

    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Имя"
    )
    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Фамилия"
    )
    middle_name = models.CharField(
        max_length=256,
        blank=True,
        default='',
        verbose_name="Отчество"
    )
    birthday = models.DateField(
        blank=False,
        verbose_name="Дата рождения",
        null=True
    )
    photo = models.ImageField(
        blank=True,
        verbose_name="Фото",
        null=True
    )
    ticket = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Билет"
    )
    notes = models.TextField(
        blank=True,
        verbose_name="Дополнительные заметки"
    )

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенти"

    def __str__(self):
        """
        Return the first_name plus the last_name, with a space in betwen.
        """

        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()


class Group (models.Model):
    """ Group Model """

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Название",)

    leader = models.OneToOneField(
        'Student',
        verbose_name="Староста",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,)

    notes = models.TextField(
        blank=True,
        verbose_name="Дополнительные записи",)

    class Meta:
        verbose_name = "Группа",
        verbose_name_plural = "Группы"

    def __str__(self):
        if self.leader:
            return "%s (%s %s)" % (self.title, self.leader.first_name,
                                   self.leader.last_name)
        else:
            return "%s" % (self.title,)