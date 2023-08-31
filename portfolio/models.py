from django.db import models


# Create your models here.
class TechStack(models.Model):
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.name}'


class SocialLink(models.Model):
    social = models.CharField(max_length=255)
    link = models.CharField(max_length=1000)
    icon = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.social}'


class Project(models.Model):
    image = models.CharField(max_length=1000)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1500)
    link = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.name}'
