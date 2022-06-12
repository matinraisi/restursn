from pickle import TRUE
from django.db import models
from django.utils.translation import gettext as _

class Reserv(models.Model):
    name = models.CharField(_('نام و نام خانوادگی '), max_length=50)
    email = models.EmailField(_('پست الکترونیکی '), max_length=50)
    phone = models.CharField(_('تلفن همراه '), max_length=13)
    date = models.DateField(_('تاریخ '))
    time = models.TimeField(_('ساعت '), null=True)
    person = models.IntegerField(_('تعداد '), default=0, null=True)

    def __str__(self):
        return self.name