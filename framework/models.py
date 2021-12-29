from django.db import models

# Create your models here.

class user_changes(models.Models):

class Superskill(models.Model):
    meta_description = 
    global_id = 
    tags = #list #local_id
    prerequisites = #list #local_id
    subskills = #list #local_id
    changes = #class

class Subskill(models.Model):
    meta_description =
    global_id = 
    tags = #list #local_id
    prerequisites = #list #local_id
    topics = #list #local_id
    changes = #class
    superskills_backlink = #list #global_id #local_id