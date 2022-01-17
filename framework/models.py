from django.db import models
from .models import Vote
# Create your models here.

class user_changes(models.Models):
    pass

# class vote(models.Model):
#     pass


class Resource(models.Model):
    link = models.TextField(blank=True)
    # resource_vote = models.OneToOneField(Vote,default=0, related_name="vote_resource", parent_link=True, blank=True, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.link

class Tag(models.Model):
    tagName = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.tagName


class Prerequisite(models.Model):
    prereqName = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.prereqName


class Topic(models.Model, Vote):
    tag_name = models.CharField(max_length=100)
    meta_description = models.CharField(max_length=200, blank=True)
    tags = models.ManyToManyField(Tag, related_name="topic_tags", blank=True)
    prerequisites = models.ManyToManyField(
        Prerequisite, related_name="topic_with_this_prerequisite", blank=True)
    topic = models.CharField(max_length=100)
    subtopics = models.ManyToManyField("self", on_delete=models.CASCADE, blank=True,  related_name="Subtopics", symmetrical=False)
    resources = models.ManyToManyField(Resource, blank=True)
    timed_changes = models.DateTimeField(auto_now_add=True)
    # subskills_backlink = 
    # topics_backlink =

class Subskill(models.Model, Vote):
    subskill_name = models.CharField(max_length=100)
    meta_description = models.CharField(max_length=200, blank=True)
    tags = models.ManyToManyField(Tag, related_name="subskill_tags", blank=True)
    prerequisites = models.ManyToManyField(Prerequisite, related_name="subskill_prerequisites", blank=True)
    topics = models.ManyToManyField(Topic, related_name="subskill_topics", blank=True)
    timed_changes = models.DateTimeField(auto_now_add=True)
    # superskills_backlink = models.ForeignKey(Superskill)

class Superskill(models.Model, Vote):
    superskill_name = models.CharField(max_length=100)
    meta_description = models.CharField(max_length=200, blank=True)
    tags = models.ManyToManyField(
        Tag, related_name="all_skills_with_this_tag", blank=True)
    prerequisites = models.ManyToManyField(
        Prerequisite, related_name="all_skills_with_this_prerequisite", blank=True)
    subskills = models.ManyToManyField(
        Subskill, related_name="super_skill", blank=True)
    timed_changes = models.DateTimeField(auto_now_add=True)





