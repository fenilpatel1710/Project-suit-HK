# Generated by Django 3.0.5 on 2020-07-31 02:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Rooms', '0029_remove_deepclean_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='deepclean',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
