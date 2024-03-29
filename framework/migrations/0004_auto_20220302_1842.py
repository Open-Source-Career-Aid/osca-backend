# Generated by Django 3.2.5 on 2022-03-02 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('framework', '0003_rename_topicname_topic_topic_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='subskill',
            name='subskill_sub',
            field=models.ManyToManyField(blank=True, related_name='subskills_under_subskill', to='framework.Subskill'),
        ),
        migrations.AddField(
            model_name='superskill',
            name='sub_superskills',
            field=models.ManyToManyField(blank=True, related_name='nested_Superskills', to='framework.Superskill'),
        ),
    ]
