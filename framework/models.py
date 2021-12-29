from django.db import models

# Create your models here.

class user_changes(models.Models):

class vote(models.Model):

class Superskill(models.Model):
    superskill_name = models.CharField(max_length=100)
    meta_description = models.CharField(max_length=200, blank=True)
    tags = #list #local_id
    prerequisites = #list #local_id
    subskills = #list #local_id
    timed_changes = #class

class Subskill(models.Model):
    subskill_name = models.CharField(max_length=100)
    meta_description = models.CharField(max_length=200, blank=True)
    tags = models.ManyToManyField(Tag, related_name="subskill_tags", blank=True)
    prerequisites = models.ManyToManyField(Prerequisite, related_name="subskill_prerequisites", blank=True)
    topics = models.ManyToManyField(Topic, related_name="subskill_topics", blank=True)
    timed_changes = #class
    superskills_backlink = #list #global_id #local_id
    votes = #class

class Topic(models.Model):
    tag_name = models.CharField(max_length=100)
    meta_description = models.CharField(max_length=200, blank=True)
    tags =
    prerequisites = 
    topics = 
    resources = #list #local_id
    timed_changes = 
    subskills_backlink = 
    topics_backlink =
    votes =

class resource(models.Model):

class Tag(models.Model):

class Prerequisite(models.Model):
