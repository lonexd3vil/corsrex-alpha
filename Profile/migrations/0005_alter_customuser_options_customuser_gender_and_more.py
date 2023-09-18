# Generated by Django 4.2.3 on 2023-08-03 07:47

from django.conf import settings
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0004_remove_customuser_phone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'User Profile'},
        ),
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.TextField(choices=[('He/Him', 'he/him'), ('She/Her', 'she/her')], default='unspecified'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.CreateModel(
            name='userGenre',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True, null=True)),
                ('genreName', models.CharField(default='', max_length=299)),
                ('genreUser', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Genre',
            },
        ),
    ]