# Generated by Django 3.0.5 on 2020-08-25 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rooms', '0016_auto_20200617_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=140)),
                ('comment1', models.CharField(max_length=140)),
            ],
        ),
    ]
