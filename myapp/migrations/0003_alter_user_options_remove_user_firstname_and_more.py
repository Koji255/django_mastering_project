# Generated by Django 5.1.2 on 2024-10-27 06:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_name_user_firstname_user_lastname'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['account_creation_date']},
        ),
        migrations.RemoveField(
            model_name='user',
            name='firstname',
        ),
        migrations.AddField(
            model_name='user',
            name='account_creation_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 27, 6, 27, 55, 450754, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='123456', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='surname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
    ]