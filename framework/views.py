# Create your views here.

from django.db.models.fields import EmailField
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from json import loads
from django.db.models import F

# For getting all the skills

@api_view(['GET'])
def get_all_skills(request):
    skills = Skill.objects.all()
    serialized_data = SkillSerializer(skills, many=True)
    return Response(serialized_data.data)

# For Getting all skills

@api_view(['GET'])
def get_all_super_skills(request):
    skills = Superskill.objects.all()
    serialized_data = SuperSkillSerializer(skills, many=True)
    return Response(serialized_data.data)

# for getting superskill with id

@api_view(['GET'])
def get_super_skill(request):
    id = request.GET.get('id')
    super_skills = Superskill.objects.filter(id=id)
    serialized_superskill_data = SuperSkillSerializer(super_skills, many=True)
    if(serialized_superskill_data.data):
        return Response(serialized_superskill_data.data[0])
    return Response(status=status.HTTP_404_NOT_FOUND)

# For getting skills with id

@api_view(['GET'])
def get_skill(request):
    id = request.GET.get('id')
    skills = Skill.objects.filter(id=id)
    serialized_skill_data = SkillSerializer(skills, many=True)
    if(serialized_skill_data.data):
        return Response(serialized_skill_data.data[0])
    return Response(status=status.HTTP_404_NOT_FOUND)

# Posting a new skill

@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def post_skill(request):
    data = request.data
    name = data['userName']
    email = data['email']
    # password = data['password']
    user = User(name=name, email=email)
    # user.save()

    skill_name = data['skill']
    skill_language = data['language']
    skill_meta_description = data['meta_description']

    try :
        user_id = User.objects.get(email=email)
    except User.DoesNotExist:
        user.save()
        user_id = User.objects.get(email=email)

    skill = Skill( skill_name=skill_name, language=skill_language, meta_description=skill_meta_description)
    skill.save()
    skill.contributed_by.add(user_id)
    skill.save()
    # for tag in data['tags']:
    #     tagObj = Tag.objects.filter(tagName=tag['tagName'])
    #     if not tagObj:
    #         tagObj = Tag.objects.create(tagName=tag['tagName'].lower())
    #         skill.tags.add(tagObj)
    #     else:
    #         skill.tags.add(tagObj[0])
    #     skill.save()

    # for prereq in data['prerequisites']:
    #     pre = Prerequisite.objects.filter(prereqName=prereq['prereqName'])
    #     if not pre:
    #         pre = Prerequisite.objects.create(
    #             prereqName=prereq['prereqName'].lower())
    #         skill.prerequisites.add(pre)
    #     else:
    #         skill.prerequisites.add(pre[0])
    #     skill.save()

    def save_prerequisites(skill_temp,data_temp):
        for prereq in data_temp['prerequisites']:
            pre = Prerequisite.objects.filter(prereqName=prereq['prereqName'])
            if not pre:
                pre = Prerequisite.objects.create(
                    prereqName=prereq['prereqName'].lower())
                skill_temp.prerequisites.add(pre)
            else:
                skill_temp.prerequisites.add(pre[0])
            skill_temp.save()
        return skill_temp

    def save_tags(skill_temp, data_temp):
        for tag in data_temp['tags']:
            tagObj = Tag.objects.filter(tagName=tag['tagName'])
            if not tagObj:
                tagObj = Tag.objects.create(tagName=tag['tagName'].lower())
                skill_temp.tags.add(tagObj)
            else:
                skill_temp.tags.add(tagObj[0])
            skill_temp.save()
    
    

    def save_nested_topics(skill_temp, data_temp):
        try:
            for topic in data_temp['topics']:
                val = topic['topicName']
                # temp2_vote = Vote()
                top = Topic(topic_name=val)
                try:
                    topic_meta_description_temp = topic['meta_description']
                    top(meta_description=topic_meta_description_temp)
                except KeyError:
                    pass
                try:
                    save_tags(top,topic)
                except KeyError:
                    pass
                try :
                    save_prerequisites(top,topic)
                except KeyError:
                    pass
                # temp2_vote.save()

                top.save()
                try:
                    for resource in topic['resources']:
                        # temp3_vote = Vote()
                        res = Resource(link=resource['link'])
                        # temp3_vote.save()
                        res.save()
                        top.resources.add(res)
                        top.save()
                except KeyError:
                    pass
                save_nested_topics(top, topic)
                if skill_temp.__class__.__name__=='Skill': 
                    skill_temp.topics.add(top)
                else :
                    skill_temp.subtopics.add(top)
        except KeyError:
            pass
    def save_nested_skill(skill_temp1,nested_data):
        try:
            for subskill in nested_data['subskills']:
                skill_name_temp = subskill['skill']
                skill_language_temp = subskill['language']
                skill_meta_description_temp = subskill['meta_description']
                skill_temp = Skill(contributed_by=user, skill=skill_name_temp, language=skill_language_temp,meta_description=skill_meta_description_temp)
                try:
                    save_tags(skill_temp,subskill)
                except KeyError:
                    pass
                try:
                    save_prerequisites(skill_temp, subskill)
                except KeyError:
                    pass
                skill_temp.save()
                try :
                    save_nested_topics(skill_temp, nested_data)
                except KeyError:
                    pass
                try :
                    save_nested_skill(skill_temp,subskill)
                except KeyError:
                    pass
                skill_temp1.subskills.add(skill_temp,subskill['subskill'])
        except KeyError:
            pass

    save_prerequisites(skill,data)
    skill.save()
    save_tags(skill, data)
    skill.save()
    
    save_nested_topics(skill, data)
    skill.save()
    save_nested_skill(skill, data)
    skill.save()

    
    return Response(status=status.HTTP_201_CREATED)
