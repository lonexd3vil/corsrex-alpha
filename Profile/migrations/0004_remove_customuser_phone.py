# Generated by Django 4.2.3 on 2023-08-03 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0003_alter_customuser_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='phone',
        ),
    ]
