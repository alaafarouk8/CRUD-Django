# Generated by Django 4.0.1 on 2022-02-02 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_intake_track_trainee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainee',
            name='intakeid',
        ),
        migrations.RemoveField(
            model_name='trainee',
            name='trackid',
        ),
    ]
