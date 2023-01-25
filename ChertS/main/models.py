from django.db import models
from PIL import Image
from os import path
# Create your models here.
from django.urls import reverse


class News(models.Model):
    title = models.CharField('Сноска', max_length=255)
    Text = models.CharField('Текст', max_length=500)
    news_photo = models.ImageField(upload_to='photos/%y/%m/%d/',null=True)
    is_published = models.BooleanField(default=True,verbose_name='Публикация')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    def save(self):
        super().save()
        img = Image.open(self.news_photo.path)

        if img.height > 500 or img.width > 700:
            output_size = (700, 400)
            img.thumbnail(output_size)
            img.save(self.news_photo.path)


    def get_absolute_url(self):
        return reverse ('post', kwargs={'post_id':self.pk})