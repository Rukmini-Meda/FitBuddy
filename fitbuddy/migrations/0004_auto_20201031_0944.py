# Generated by Django 3.0.5 on 2020-10-31 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitbuddy', '0003_fitnesscenter_fitnesscenter_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fitnesscenter',
            name='fitnesscenter_name',
            field=models.CharField(max_length=30),
        ),
    ]