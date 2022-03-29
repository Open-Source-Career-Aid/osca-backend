from django.urls import path

from . import views,models

urlpatterns = [
    path("get-all-skills/", views.get_all_skills,name="get all skills"),
    path("get-all-super-skills/", views.get_all_super_skills,name="get all super skills"),
    path("get-all-topics/", views.get_all_topics,name="get all topics"),
    path("get-super-skill/", views.get_super_skill,name="get super skill"),
    path("get-skill/", views.get_skill,name="get skill"),
    path("get-topic/", views.get_topic,name="get topic"),
    path("post-skill/", views.post_skill, name="post skill"),
    path("post-r-skill-skills/", views.post_relatation_skill_skill, name="post Relation skill - skills"),
    path("post-r-skill-topics/", views.post_relatation_skill_topics, name="post Relation skill- topics"),
    path("post-super-skill/", views.post_super_skill, name="post Super skill"),
    path("post-r-superskill-skills/", views.post_relatation_superskill_skill, name="post Realtion Super_skill-skills"),
    path("post-r-superskill-superskills/", views.post_relatation_superskill_superskill, name="post Relation Super_skill Super_skills"),
    path("post-topic/", views.post_topic, name="post topic"),
    path("post-r-topic-topics/", views.post_relatation_topic_topic, name="post Relation topic-topics"),



]
