from django.contrib import admin

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Resource)
admin.site.register(Tag)
admin.site.register(Prerequisite)
admin.site.register(Topic)
admin.site.register(Subskill)
admin.site.register(Superskill)




