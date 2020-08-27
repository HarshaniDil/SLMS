# Generated by Django 3.0.7 on 2020-07-04 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0007_apply_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=200),
        ),
    ]