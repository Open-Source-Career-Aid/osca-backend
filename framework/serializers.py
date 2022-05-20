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
        fields = ['id','link']
        # fields='__all__'

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = []
        # fields='__all__'

class TopicSerializer(serializers.ModelSerializer):
    resources=ResourceSerializer(read_only=True, many=True)
    class Meta:
        model = Topic
        fields = ['id','topic_name','tags','subtopics','resources']
        depth=1
        # fields='__all__'
    def get_fields(self):
        fields=super(TopicSerializer, self).get_fields()
        fields['subtopics'] = TopicSerializer(many=True)
        return fields

class SkillSerializer(serializers.ModelSerializer):
    # prerequisite = RelationalPrerequisiteSerializer(source="prerequisites",read_only=True, many=True)
    # subskills=SkillSerializer()
    topics=TopicSerializer(read_only=True, many=True)
    class Meta:
        model = Skill
        # fields='__all__'
        fields = ['id','skill_name','tags','topics','subskills']
        depth=1
    
    def get_fields(self):
        fields=super(SkillSerializer, self).get_fields()
        fields['subskills'] = SkillSerializer(many=True)
        return fields
        # depth = 4

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = []

        # fields='__all__'

class SuperSkillSerializer(serializers.ModelSerializer):
    # sub_skill= RelationalSubSkillSerializer(source="Skills",read_only=True, many=True)
    # sub_superskills=SuperSkillSerializer()
    class Meta:
        model = Superskill
        fields = ['id','superskill_name','tags','Skills','sub_superskills']
        # fields = '__all__'
        depth=2

    def get_fields(self):
        fields=super(SuperSkillSerializer, self).get_fields()
        fields['sub_superskills'] = SuperSkillSerializer(many=True)
        return fields
        

class SkillNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id','skill_name','tags']
        depth=2

class SuperSkillNameSerializer(serializers.ModelSerializer):
    tag = TagSerializer(source="tags",read_only=True, many=True)
    sub_skills= RelationalSubSkillSerializer(source="skills",read_only=True, many=True)
    class Meta:
        model = Superskill
        fields = ['id','superskill_name','tags','sub_skills']
        
    def get_fields(self):
        fields=super(SuperSkillNameSerializer, self).get_fields()
        fields['sub_superskills'] = SuperSkillNameSerializer(many=True)
        return fields

# class SuperSkillNameSerializer2(serializers.ModelSerializer):
#     class Meta:
#         model = Super_skill
#         fields = ['id','name','tags']
#         depth=2
