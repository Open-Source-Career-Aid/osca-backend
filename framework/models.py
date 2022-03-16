from django.db import models
from vote.models import VoteModel
from user.models import User
# Create your models here.

class user_changes(models.Model):
    pass

# class vote(models.Model):
#     pass


class Resource(VoteModel):
    link = models.TextField(blank=True)
<<<<<<< Updated upstream
    # resource_vote = models.OneToOneField(Vote,default=0, related_name="vote_resource", parent_link=True, blank=True, on_delete=models.PROTECT)
    # topics
    # type/class of the resource

=======
    #resource_vote = models.OneToOneField(Vote,default=0, related_name="vote_resource", parent_link=True, blank=True, on_delete=models.PROTECT)
    
>>>>>>> Stashed changes
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


class Topic( VoteModel):
    meta_description = models.CharField(max_length=200, blank=True)
    tags = models.ManyToManyField(Tag, related_name="topic_tags", blank=True)
    prerequisites = models.ManyToManyField(
        Prerequisite, related_name="topic_with_this_prerequisite", blank=True)
<<<<<<< Updated upstream
    topic_name = models.CharField(max_length=100)
    contributed_by = models.ManyToManyField(User, blank=True)
    subtopics = models.ManyToManyField("self", blank=True,  related_name="Subtopics", symmetrical=False)
    resources = models.ManyToManyField(Resource, blank=True)
    timed_changes = models.DateTimeField(auto_now_add=True)
    # subskills_backlink = 
    # topics_backlink =
    def __str__(self):
        return self.topic_name

class Skill( VoteModel):
    skill_name = models.CharField(max_length=100)
    language = models.CharField(max_length=200, blank=True)
    contributed_by = models.ManyToManyField(User, blank=True)
=======
    topics = models.CharField(max_length=100)
    resources = models.ManyToManyField(
        Resource, related_name="resources_topic", blank=True)
    #timed_changes = 
    #subskills_backlink = 
    #topics_backlink =
    #votes =

class Subskill(models.Model):
    subskill_name = models.CharField(max_length=100)
>>>>>>> Stashed changes
    meta_description = models.CharField(max_length=200, blank=True)
    tags = models.ManyToManyField(Tag, related_name="subskill_tags", blank=True)
    prerequisites = models.ManyToManyField(Prerequisite, related_name="subskill_prerequisites", blank=True)
    topics = models.ManyToManyField(Topic, related_name="subskill_topics", blank=True)
<<<<<<< Updated upstream
    timed_changes = models.DateTimeField(auto_now_add=True)
    # superskills_backlink = models.ForeignKey(Superskill)
    subskills = models.ManyToManyField("self", blank=True, related_name="subskills_under_subskill", symmetrical=False)
    def __str__(self):
        return self.skill_name
=======
    #timed_changes = #class
    #uperskills_backlink = #list #global_id #local_id
    #votes = #class
>>>>>>> Stashed changes

class Superskill( VoteModel):
    superskill_name = models.CharField(max_length=100)
    meta_description = models.CharField(max_length=200, blank=True)
    language = models.CharField(max_length=200, blank=True)
    contributed_by = models.ManyToManyField(User, blank=True)
    tags = models.ManyToManyField(
        Tag, related_name="all_skills_with_this_tag", blank=True)
    prerequisites = models.ManyToManyField(
        Prerequisite, related_name="all_skills_with_this_prerequisite", blank=True)
<<<<<<< Updated upstream
    sub_superskills = models.ManyToManyField("self", blank=True, related_name="nested_Superskills", symmetrical=False)
    Skills = models.ManyToManyField(
        Skill, related_name="super_skill", blank=True)
    timed_changes = models.DateTimeField(auto_now_add=True)
=======
    subskills = models.ManyToManyField(
        Subskill, related_name="super_skill", blank=True)
    #timed_changes = #class
>>>>>>> Stashed changes

    def __str__(self):
        return self.superskill_name




