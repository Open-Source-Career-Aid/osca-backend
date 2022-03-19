# Generated by Django 3.2.4 on 2022-03-19 03:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('framework', '0012_auto_20220319_0206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='contributed_by',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='language',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='meta_description',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='subskills',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='timed_changes',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='resources',
        ),
        migrations.AddField(
            model_name='topic',
            name='skills_backlink',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='framework.skill'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Resource',
        ),
    ]
