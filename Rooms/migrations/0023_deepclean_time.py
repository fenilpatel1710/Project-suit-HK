# Generated by Django 3.0.5 on 2020-07-31 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rooms', '0022_deepclean_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='deepclean',
            name='time',
            field=models.TimeField(auto_now=bool),
            preserve_default=bool,
        ),
    ]
