# Generated by Django 3.1.2 on 2020-11-28 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertise', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fitnessproduct',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]