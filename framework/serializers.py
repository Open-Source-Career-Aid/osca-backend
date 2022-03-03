from django.db.models import fields
from django.db.models.fields import files
from rest_framework import serializers
from .models import *
from user.models import *
from vote.models import *
from .relational_serializers import *

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields='__all__'

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields='__all__'

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields='__all__'

class SkillSerializer(serializers.ModelSerializer):
    prerequisite = RelationalPrerequisiteSerializer(source="prerequisites",read_only=True, many=True)
    class Meta:
        model = Skill
        fields='__all__'
        depth = 4

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'

class SuperSkillSerializer(serializers.ModelSerializer):
    sub_skill= RelationalSubSkillSerializer(source="Skills",read_only=True, many=True)
    class Meta:
        model = Superskill
        fields = '__all__'
        depth=3

class SkillNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id','skill_name','tags']
        depth=2

class SuperSkillNameSerializer(serializers.ModelSerializer):
    tag = TagSerializer(source="tags",read_only=True, many=True)
    sub_skill= RelationalSubSkillSerializer(source="skills",read_only=True, many=True)
    class Meta:
        model = Superskill
        fields = ['id','superskill_name','tags','subskills']

# class SuperSkillNameSerializer2(serializers.ModelSerializer):
#     class Meta:
#         model = Super_skill
#         fields = ['id','name','tags']
#         depth=2
