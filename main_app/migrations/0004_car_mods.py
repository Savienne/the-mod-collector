# Generated by Django 4.1 on 2022-08-09 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_mod'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='mods',
            field=models.ManyToManyField(to='main_app.mod'),
        ),
    ]
