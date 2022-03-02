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
