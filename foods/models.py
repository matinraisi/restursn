from django.db import models
from django.utils.translation import gettext as _



class Foods(models.Model):
    FOOD_TYPE = [
        ("drink" , "نوشیدنی"),
        ("breakfast" , "صبحانه"),
        ("lunch" , "ناهار"),
        ("dinner" , "شام")
    ]
    name = models.CharField(_('نام '),max_length=30)
    descriptions = models.CharField(_('توضیحات '),max_length=255)
    price = models.IntegerField(_('قیمت '),default=0)
    photo = models.ImageField(_("عکس"),upload_to = 'image/')
    type_food =models.CharField(_("نوع غذا"), max_length=10, choices=FOOD_TYPE, default="breakfast")

    def __str__(self):
        return self.name