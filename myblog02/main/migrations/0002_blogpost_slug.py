# Generated by Django 4.1.1 on 2022-09-13 07:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, editable=False, max_length=180, unique=True, verbose_name='Slug'),
        ),
    ]
