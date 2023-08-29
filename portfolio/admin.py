from django.contrib import admin

from .models import SocialLink, TechStack

# Register your models here.
admin.site.register(TechStack)
admin.site.register(SocialLink)
