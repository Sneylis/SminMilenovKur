from PIL import Image
from django.db import models

# Create your models here.
from django.urls import reverse


class Books (models.Model):
    title = models.CharField('Название', max_length=250)
    author = models.CharField('Автор', max_length=50)
    preview = models.TextField('О книге',max_length=500)
    photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT,null=True)
    file = models.FileField(upload_to='books/%y/%m/%d/',null=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    def save(self):
        super().save()
        img = Image.open(self.photo.path)

        if img.height > 500 or img.width > 700:
            output_size = (700, 400)
            img.thumbnail(output_size)
            img.save(self.photo.path)

    def get_absolute_url(self):
        return reverse ('sbook', kwargs={'sbook_id':self.pk})

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
