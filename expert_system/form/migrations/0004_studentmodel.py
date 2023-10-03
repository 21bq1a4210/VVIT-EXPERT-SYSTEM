# Generated by Django 3.2.18 on 2023-10-03 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_delete_studentmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('registration', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('counsellor', models.CharField(max_length=200)),
            ],
        ),
    ]
