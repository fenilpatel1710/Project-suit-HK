# Generated by Django 3.0.5 on 2020-04-24 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rooms', '0006_roomfloor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='room_floor',
        ),
        migrations.AddField(
            model_name='room',
            name='rroom_floor',
            field=models.CharField(choices=[('1st floor', '1st floor'), ('2nd floor', '2nd floor'), ('3rd floor', '3rd floor')], default='1st floor', max_length=50),
        ),
    ]
