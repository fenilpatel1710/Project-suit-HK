# Generated by Django 3.0.5 on 2020-07-31 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Rooms', '0026_auto_20200731_0151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deepclean',
            name='date',
        ),
    ]