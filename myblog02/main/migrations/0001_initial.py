# Generated by Django 4.1.1 on 2022-09-13 10:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Name')),
                ('slug', models.SlugField(default=django.utils.timezone.now, editable=False, max_length=180, unique=True, verbose_name='Slug')),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Title')),
                ('slug', models.SlugField(default=django.utils.timezone.now, editable=False, max_length=180, unique=True, verbose_name='Slug')),
                ('content', models.TextField(max_length=800, verbose_name='Content')),
                ('banner', models.ImageField(blank=True, default='images/default_image.png', null=True, upload_to='images/', verbose_name='Image')),
                ('tags', models.ManyToManyField(to='main.blogtag', verbose_name='Tags')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
        ),
    ]
