# Generated by Django 3.1.3 on 2020-12-05 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_about_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='slug',
        ),
    ]
