# Generated by Django 3.0.7 on 2020-07-21 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0023_auto_20200721_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
    ]
