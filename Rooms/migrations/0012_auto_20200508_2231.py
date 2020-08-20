# Generated by Django 3.0.5 on 2020-05-08 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rooms', '0011_room_room_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_status',
            field=models.CharField(choices=[('clean', 'clean'), ('Dirty', 'Dirty'), ('Maintenance', 'Maintenance')], default='Maintenance', max_length=50),
        ),
    ]
