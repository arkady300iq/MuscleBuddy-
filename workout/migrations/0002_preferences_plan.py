# Generated by Django 5.1.2 on 2024-11-30 11:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0001_initial'),
        ('workout_plan', '0003_remove_trainingday_name_trainingday_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='preferences',
            name='plan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='workout_plan.trainingplan'),
            preserve_default=False,
        ),
    ]
