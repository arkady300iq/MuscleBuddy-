# Generated by Django 5.1.2 on 2024-12-24 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0006_exercise_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='order',
        ),
    ]
