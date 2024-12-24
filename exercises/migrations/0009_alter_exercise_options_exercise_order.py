# Generated by Django 5.1.2 on 2024-12-24 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0008_remove_exercise_description_set'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exercise',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='exercise',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
