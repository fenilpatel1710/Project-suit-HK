# Generated by Django 3.0.5 on 2020-04-24 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_number',
            field=models.CharField(default='SOME STRING', max_length=140),
        ),
    ]