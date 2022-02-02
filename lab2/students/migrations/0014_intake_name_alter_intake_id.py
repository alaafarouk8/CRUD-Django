# Generated by Django 4.0.1 on 2022-02-02 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0013_remove_intake_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='intake',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='intake',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
