# Generated by Django 4.2.5 on 2023-09-27 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='fitnessGoal',
            field=models.CharField(choices=[('generalfitness', 'General Fitness'), ('balance', 'Balance'), ('posture', 'Posture'), ('strength', 'Strength')], default='strength', max_length=255),
        ),
    ]