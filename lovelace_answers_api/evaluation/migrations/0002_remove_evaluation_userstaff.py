# Generated by Django 5.1.7 on 2025-03-26 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluation',
            name='userStaff',
        ),
    ]
