# Generated by Django 3.2.4 on 2022-01-21 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='admin',
            new_name='is_staff',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='team',
            new_name='is_superuser',
        ),
    ]
