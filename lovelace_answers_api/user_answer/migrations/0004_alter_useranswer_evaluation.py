# Generated by Django 5.1.7 on 2025-04-10 12:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0003_alter_evaluation_test_results'),
        ('user_answer', '0003_usercheckboxexerciseanswer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswer',
            name='evaluation',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='evaluation.evaluation'),
        ),
    ]
