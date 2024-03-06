from django.db import models

class Post (models.Model):
    json = models.JSONField()


