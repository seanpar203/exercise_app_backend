# Generated by Django 4.2.5 on 2023-09-27 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_app', '0009_rename_workoutlocation_exercise_workout_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='fitnessGoal',
            new_name='fitness_goal',
        ),
    ]