# Generated by Django 4.2.3 on 2023-09-18 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0010_customuser_is_supreme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_paid',
        ),
    ]