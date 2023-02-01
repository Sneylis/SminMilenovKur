from django.db import models

# Create your models here.
from django.urls import reverse


class VacationFile(models.Model):
    FirstName = models.CharField('Имя',max_length=255)
    SecondName = models.CharField('Фамилия',max_length=255)
    Resume = models.FileField(upload_to='vacations/%y/%m/%d/',null=True)
    Atestat = models.FileField(upload_to='vacations/%y/%m/%d/',null=True)
    About = models.TextField('Расскажите о себе',max_length=255)

    class Meta:
        verbose_name = 'РЕЗЮМЕ'
        verbose_name_plural = "РЕЗЮМЕ"

    def __str__(self):
        return self.FirstName

class Vacations (models.Model):
    title = models.CharField(max_length=255)
    about = models.TextField(max_length=255)
    cat =  models.ForeignKey('VacationsCategory',on_delete=models.PROTECT,null=True)
    def get_absolute_url(self):
            return reverse ('vac', kwargs={'vac_id':self.pk})
    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return self.title





class VacationsCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = "категории"