# Generated by Django 4.0.5 on 2022-06-15 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='rapid_api_key',
        ),
    ]
