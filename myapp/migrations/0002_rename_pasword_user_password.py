# Generated by Django 4.0.2 on 2022-02-03 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='pasword',
            new_name='password',
        ),
    ]
