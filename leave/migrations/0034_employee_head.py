# Generated by Django 3.0.7 on 2020-08-13 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0033_remove_employee_head'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='head',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='leave.head'),
        ),
    ]
