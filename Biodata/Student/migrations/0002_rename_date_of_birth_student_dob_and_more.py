# Generated by Django 5.0.3 on 2024-03-28 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='date_of_birth',
            new_name='dob',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='first_name',
            new_name='f_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='last_name',
            new_name='l_name',
        ),
    ]
