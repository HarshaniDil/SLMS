# Generated by Django 3.0.7 on 2020-08-13 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0037_auto_20200813_2206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='head',
        ),
    ]