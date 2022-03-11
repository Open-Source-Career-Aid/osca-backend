# Generated by Django 3.2.4 on 2022-03-11 08:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('framework', '0006_auto_20220303_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='superskill',
            name='contributed_by',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='superskill',
            name='language',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='topic',
            name='contributed_by',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
