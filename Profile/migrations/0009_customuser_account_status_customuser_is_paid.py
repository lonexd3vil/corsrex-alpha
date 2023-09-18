# Generated by Django 4.2.3 on 2023-08-03 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0008_osinformation'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='account_status',
            field=models.CharField(choices=[('Active', 'active'), ('Inactive', 'inactive')], default='Inactive', max_length=30),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]
