# Generated by Django 2.0 on 2021-07-14 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='fooditem',
            name='updates_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='restaurants',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='restaurants',
            name='updates_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
