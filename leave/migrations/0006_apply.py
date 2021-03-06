# Generated by Django 3.0.7 on 2020-07-03 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0005_leave'),
    ]

    operations = [
        migrations.CreateModel(
            name='apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('designation', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('phoneno', models.CharField(max_length=200, null=True)),
                ('from_date', models.DateField(null=True)),
                ('to_date', models.DateField(null=True)),
                ('from_time', models.TimeField(null=True)),
                ('to_time', models.TimeField(null=True)),
                ('reason', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('leave', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='leave.leave')),
            ],
        ),
    ]
