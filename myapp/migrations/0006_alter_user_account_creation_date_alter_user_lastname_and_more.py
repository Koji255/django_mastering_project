# Generated by Django 5.1.2 on 2024-10-27 06:52

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_user_account_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='account_creation_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 27, 6, 52, 2, 777560, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastname',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default=None, max_length=24, validators=[django.core.validators.MinLengthValidator(8)]),
        ),
        migrations.AlterField(
            model_name='user',
            name='surname',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
