# Generated by Django 3.0.6 on 2020-05-26 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
    migrations.RenameField('Task', 'created', 'finished'),
    migrations.RenameField('Task', 'completed', 'created'),
    ]
