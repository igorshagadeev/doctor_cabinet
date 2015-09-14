# -*- coding: utf-8 -*-



from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(
        max_length = 128,
        verbose_name=u"имя",
        blank=False,
        default = '',
    )
    available = models.BooleanField(
        default=True,
        verbose_name=u"доступен",
    )

    def __str__(self):
        return str(self.id) + ' ' + self.name