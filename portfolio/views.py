from django.shortcuts import render

from .models import SocialLink, TechStack


def index(request):
    tech_stacks = TechStack.objects.all()
    social_links = SocialLink.objects.all()
    return render(request, 'portfolio/index.html', {'tech_stack': tech_stacks, 'social_link': social_links})
