from django.contrib import admin

from .models import Project, SocialLink, TechStack

# Register your models here.
admin.site.register(TechStack)
admin.site.register(SocialLink)
admin.site.register(Project)
