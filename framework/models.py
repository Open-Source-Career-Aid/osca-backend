from django.db import models

# Create your models here.

class user_changes(models.Models):

class vote(models.Model):

class Superskill(models.Model):
    meta_description = 
    global_id = 
    tags = #list #local_id
    prerequisites = #list #local_id
    subskills = #list #local_id
    timed_changes = #class

class Subskill(models.Model):
    meta_description =
    global_id = 
    tags = #list #local_id
    prerequisites = #list #local_id
    topics = #list #local_id
    timed_changes = #class
    superskills_backlink = #list #global_id #local_id
    votes = #class

class topic(models.Model):
    meta_description = 
    global_id = 
    tags =
    prerequisites = 
    topics = 
    resources = #list #local_id
    timed_changes = 
    subskills_backlink = 
    topics_backlink =
    votes =