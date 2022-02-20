# Generated by Django 3.2.5 on 2022-02-19 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prerequisite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prereqName', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subskill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_score', models.IntegerField(db_index=True, default=0)),
                ('num_vote_up', models.PositiveIntegerField(db_index=True, default=0)),
                ('num_vote_down', models.PositiveIntegerField(db_index=True, default=0)),
                ('subskill_name', models.CharField(max_length=100)),
                ('meta_description', models.CharField(blank=True, max_length=200)),
                ('timed_changes', models.DateTimeField(auto_now_add=True)),
                ('prerequisites', models.ManyToManyField(blank=True, related_name='subskill_prerequisites', to='framework.Prerequisite')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagName', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='user_changes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_score', models.IntegerField(db_index=True, default=0)),
                ('num_vote_up', models.PositiveIntegerField(db_index=True, default=0)),
                ('num_vote_down', models.PositiveIntegerField(db_index=True, default=0)),
                ('Topic_name', models.CharField(max_length=100)),
                ('meta_description', models.CharField(blank=True, max_length=200)),
                ('topicname', models.CharField(max_length=100)),
                ('timed_changes', models.DateTimeField(auto_now_add=True)),
                ('prerequisites', models.ManyToManyField(blank=True, related_name='topic_with_this_prerequisite', to='framework.Prerequisite')),
                ('resources', models.ManyToManyField(blank=True, to='framework.Resource')),
                ('subtopics', models.ManyToManyField(blank=True, related_name='Subtopics', to='framework.Topic')),
                ('tags', models.ManyToManyField(blank=True, related_name='topic_tags', to='framework.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Superskill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_score', models.IntegerField(db_index=True, default=0)),
                ('num_vote_up', models.PositiveIntegerField(db_index=True, default=0)),
                ('num_vote_down', models.PositiveIntegerField(db_index=True, default=0)),
                ('superskill_name', models.CharField(max_length=100)),
                ('meta_description', models.CharField(blank=True, max_length=200)),
                ('timed_changes', models.DateTimeField(auto_now_add=True)),
                ('prerequisites', models.ManyToManyField(blank=True, related_name='all_skills_with_this_prerequisite', to='framework.Prerequisite')),
                ('subskills', models.ManyToManyField(blank=True, related_name='super_skill', to='framework.Subskill')),
                ('tags', models.ManyToManyField(blank=True, related_name='all_skills_with_this_tag', to='framework.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='subskill',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='subskill_tags', to='framework.Tag'),
        ),
        migrations.AddField(
            model_name='subskill',
            name='topics',
            field=models.ManyToManyField(blank=True, related_name='subskill_topics', to='framework.Topic'),
        ),
    ]