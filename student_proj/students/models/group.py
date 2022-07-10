from django.db import models


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
        """ Возвращает имя модель в единичном и множественном числе."""
        verbose_name = "Группа",
        verbose_name_plural = "Группы"

    def __str__(self):
        """ Название модель в админ кабинете  """
        if self.leader:
            return "%s (%s %s)" % (self.title, self.leader.first_name,
                                   self.leader.last_name)
        else:
            return "%s" % (self.title,)