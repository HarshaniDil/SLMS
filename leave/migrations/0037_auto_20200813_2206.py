# Generated by Django 3.0.7 on 2020-08-13 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0036_auto_20200813_2157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='head',
            name='email',
        ),
        migrations.RemoveField(
            model_name='head',
            name='name',
        ),
        migrations.AlterField(
            model_name='head',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='leave.department'),
        ),
    ]
