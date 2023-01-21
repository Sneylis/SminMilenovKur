from django.db import models

# Create your models here.
from django.urls import reverse


class Books (models.Model):
    title = models.CharField('Название', max_length=250)
    author = models.CharField('Автор', max_length=50)
    preview = models.TextField('О книге',max_length=500)
    photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT,null=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = "Книги"


class Category (models.Model):
    name = models.CharField(max_length=100,db_index=True)

    class Meta:
        verbose_name="Категория"
        verbose_name_plural="Категории"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse ('category', kwargs={'cat_id':self.pk})
