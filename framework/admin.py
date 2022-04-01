from django.contrib import admin

from django.contrib import admin
from .models import *
from ordered_model.admin import OrderedModelAdmin
from ordered_model.admin import OrderedTabularInline, OrderedInlineModelAdminMixin



class SkillTopicTabularInline(OrderedTabularInline):
    model = SkillTopicThroughModel
    fields = ('topic', 'order', 'move_up_down_links',)
    readonly_fields = ('order', 'move_up_down_links',)
    ordering = ('order',)
    extra = 1


class ResourceAdmin(OrderedModelAdmin):
    list_display = ('link', 'move_up_down_links')
class TagAdmin(OrderedModelAdmin):
    list_display = ('tagName', 'move_up_down_links')
class PrerequisiteAdmin(OrderedModelAdmin):
    list_display = ('prereqName', 'move_up_down_links')
class TopicAdmin(OrderedModelAdmin):
    list_display = ('topic_name', 'move_up_down_links')
class SkillAdmin(OrderedInlineModelAdminMixin, OrderedModelAdmin):
    model = Skill
    list_display = ('skill_name', 'move_up_down_links')
    inlines = (SkillTopicTabularInline, )
class SuperskillAdmin(OrderedModelAdmin):
    list_display = ('superskill_name', 'move_up_down_links')

# Register your models here.
admin.site.register(Resource,ResourceAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Prerequisite,PrerequisiteAdmin)
admin.site.register(Topic,TopicAdmin)
admin.site.register(Skill,SkillAdmin)
admin.site.register(Superskill,SuperskillAdmin)




