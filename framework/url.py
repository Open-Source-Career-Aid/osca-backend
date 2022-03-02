from django.urls import path

from . import views,models

urlpatterns = [
    path("get-all-skills/", views.get_all_skills,name="get all skills"),
    path("get-all-super-skills/", views.get_all_super_skills,name="get all super skills"),
    path("get-super-skill/", views.get_super_skill,name="get super skill"),
    path("get-skill/", views.get_skill,name="get skill"),
]
