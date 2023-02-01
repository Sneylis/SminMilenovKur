# Generated by Django 4.1.5 on 2023-01-29 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VacationFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=255, verbose_name='Имя')),
                ('SecondName', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('Resume', models.FileField(null=True, upload_to='vacations/%y/%m/%d/')),
                ('Atestat', models.FileField(null=True, upload_to='vacations/%y/%m/%d/')),
                ('About', models.TextField(max_length=255, verbose_name='Расскажите о себе')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]