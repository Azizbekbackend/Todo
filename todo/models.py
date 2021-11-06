from django.db import models
import datetime


class Ish(models.Model):
    nomi = models.CharField(max_length=100)
    sana = models.DateField(default=datetime.date.today())
    vaqti = models.TimeField()
    bajarish = models.BooleanField(default=False)

    def __str__(self):
        return self.nomi

    class Meta:
        ordering = ('sana','vaqti')
        verbose_name_plural = 'Ishlar'