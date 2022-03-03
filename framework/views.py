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
    user = User(userName=name, email=email)
    user.save()

    skill_name = data['skill']
    # skill_language = data['language']
    skill = Skill(contributed_by=user, skill=skill_name, language=skill_language)
    skill.save()

    for tag in data['tags']:
        tagObj = Tag.objects.filter(tagName=tag['tagName'])
        if not tagObj:
            tagObj = Tag.objects.create(tagName=tag['tagName'].lower())
            skill.tags.add(tagObj)
        else:
            skill.tags.add(tagObj[0])
        skill.save()

    for prereq in data['prerequisites']:
        pre = Prerequisite.objects.filter(prereqName=prereq['prereqName'])
        if not pre:
            pre = Prerequisite.objects.create(
                prereqName=prereq['prereqName'].lower())
            skill.prerequisites.add(pre)
        else:
            skill.prerequisites.add(pre[0])
        skill.save()

    for level in data['levels']:
        val = level['levelName']
        # temp1_vote = Vote()
        lev = Level(levelName=val)
        lev.save()
        
        for topic in level['topics']:
            val = topic['topicName']
            temp2_vote = Vote()
            top = Topic(topicName=val, topic_vote= temp2_vote)
            temp2_vote.save()
            top.save()
            try:
                for resource in topic['resources']:
                    temp3_vote = Vote()
                    res = Resource(link=resource['link'], resource_vote = temp3_vote)
                    temp3_vote.save()
                    res.save()
                    top.resources.add(res)
                    top.save()
            except KeyError:
                pass
            lev.topics.add(top)
            try:
                for y in topic['subtopics']:
                    temp4_vote = Vote()
                    val = y['value']
                    sub = Subtopic(value=val, subtopic_vote=temp4_vote)
                    temp4_vote.save()
                    sub.save()
                    for yres in y['resources']:
                        temp5_vote = Vote()
                        res = Resource(link=yres['link'], resource_vote = temp5_vote)
                        temp5_vote.save()
                        res.save()
                        sub.resources.add(res)
                        sub.save()
                    top.subtopics.add(sub)
                    top.save()
            except KeyError:
                pass

            lev.topics.add(top)
            lev.save()
        skill.levels.add(lev)
        skill.save()
    return Response(status=status.HTTP_201_CREATED)
