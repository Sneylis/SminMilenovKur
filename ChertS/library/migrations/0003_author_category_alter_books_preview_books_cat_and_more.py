# Generated by Django 4.1.5 on 2023-01-17 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_books_options_books_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='books',
            name='preview',
            field=models.TextField(max_length=500, verbose_name='О книге'),
        ),
        migrations.AddField(
            model_name='books',
            name='cat',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.PROTECT, to='library.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='library.author'),
        ),
    ]