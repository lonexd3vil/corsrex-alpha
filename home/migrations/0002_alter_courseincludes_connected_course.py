# Generated by Django 4.2.3 on 2023-09-18 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseincludes',
            name='connected_course',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='included', to='home.courses'),
        ),
    ]