# Generated by Django 5.1.7 on 2025-03-26 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserTaskCompletion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise', models.CharField(max_length=255)),
                ('user', models.CharField(max_length=255)),
                ('instance', models.CharField(max_length=255)),
                ('points', models.DecimalField(decimal_places=5, default=0, max_digits=8)),
                ('state', models.CharField(choices=[('unanswered', 'The task has not been answered yet'), ('correct', 'The task has been answered correctly'), ('incorrect', 'The task has not been answered correctly'), ('credited', 'The task has been credited by completing another task'), ('submitted', 'An answer has been submitted, awaiting assessment'), ('ongoing', 'The task has been started')], max_length=16)),
            ],
            options={
                'unique_together': {('exercise', 'instance', 'user')},
            },
        ),
    ]
