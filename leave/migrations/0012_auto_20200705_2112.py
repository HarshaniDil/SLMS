# Generated by Django 3.0.7 on 2020-07-05 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0011_auto_20200705_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='head',
            name='department',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='department',
        ),
    ]
