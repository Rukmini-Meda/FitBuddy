# Generated by Django 3.1.3 on 2020-11-21 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitbuddy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='nutrition',
        ),
    ]