# Generated by Django 5.1.2 on 2024-12-21 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0004_alter_exercise_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='description_set',
            field=models.TextField(blank=True, null=True),
        ),
    ]