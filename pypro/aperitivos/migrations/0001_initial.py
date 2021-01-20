# Generated by Django 3.1.5 on 2021-01-19 17:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=32)),
                ('slug', models.SlugField(max_length=32)),
                ('vimeo_id', models.CharField(max_length=32)),
                ('creation', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
