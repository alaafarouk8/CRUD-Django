# Generated by Django 4.0.1 on 2022-02-02 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0011_alter_intake_intakename'),
    ]

    operations = [
        migrations.RenameField(
            model_name='intake',
            old_name='intakename',
            new_name='name',
        ),
    ]
