# django
from django.db import models

# project
from doctor.models import Doctor



class Appointment(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name=u"имя",
        blank=False,
        default='',
    )
    surname = models.CharField(
        max_length=128,
        verbose_name=u"фамилия",
        blank=False,
        default='',
    )
    patronymic = models.CharField(
        max_length=128,
        verbose_name=u"отчество",
        blank=False,
        default='',
    )
    datetime = models.DateTimeField(
        verbose_name=u"Дата"
    )
    doctor = models.ForeignKey(
        Doctor,
        blank=False,
        null=False,
        related_name='doctor',
    )

    def __str__(self):
        return str(self.id) + ' ' + self.surname + ' ' + str(self.datetime)
