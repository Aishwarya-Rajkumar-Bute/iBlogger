# Generated by Django 3.1.3 on 2020-12-05 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_remove_about_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='slug',
            field=models.CharField(default='', max_length=130),
            preserve_default=False,
        ),
    ]
