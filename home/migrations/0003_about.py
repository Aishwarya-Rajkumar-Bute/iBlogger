# Generated by Django 3.1.3 on 2020-12-04 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=225)),
                ('content', models.TextField()),
            ],
        ),
    ]
