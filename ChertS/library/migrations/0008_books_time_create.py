# Generated by Django 4.1.5 on 2023-01-25 13:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_books_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
            preserve_default=False,
        ),
    ]
