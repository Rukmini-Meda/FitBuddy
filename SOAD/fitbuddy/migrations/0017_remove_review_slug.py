# Generated by Django 3.0.5 on 2020-11-11 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitbuddy', '0016_auto_20201111_2340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='slug',
        ),
    ]