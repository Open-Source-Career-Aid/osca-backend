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

@api_view(['GET'])
def get_all_skills(request):
    skills = Subskill.objects.all()
    serialized_data = SubSkillSerializer(skills, many=True)
    return Response(serialized_data.data)

@api_view(['GET'])
def get_all_super_skills(request):
    skills = Superskill.objects.all()
    serialized_data = SuperSkillSerializer(skills, many=True)
    return Response(serialized_data.data)

@api_view(['GET'])
def get_super_skill(request):
    id = request.GET.get('id')
    super_skills = Superskill.objects.filter(id=id)
    serialized_superskill_data = SuperSkillSerializer(super_skills, many=True)
    if(serialized_superskill_data.data):
        return Response(serialized_superskill_data.data[0])
    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_skill(request):
    id = request.GET.get('id')
    skills = Subskill.objects.filter(id=id)
    serialized_skill_data = SubSkillSerializer(skills, many=True)
    if(serialized_skill_data.data):
        return Response(serialized_skill_data.data[0])
    return Response(status=status.HTTP_404_NOT_FOUND)
