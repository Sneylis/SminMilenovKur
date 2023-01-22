# Generated by Django 4.1.5 on 2023-01-18 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Сноска')),
                ('Text', models.CharField(max_length=500, verbose_name='Текст')),
                ('news_photo', models.ImageField(null=True, upload_to='photos/%y/%m/%d/')),
            ],
        ),
    ]