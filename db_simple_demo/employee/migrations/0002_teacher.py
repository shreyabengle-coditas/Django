# Generated by Django 5.0.3 on 2024-03-26 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.IntegerField()),
                ('teacher_name', models.CharField(max_length=30)),
                ('teacher_last_name', models.CharField(max_length=30)),
            ],
        ),
    ]
