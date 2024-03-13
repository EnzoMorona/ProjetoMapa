from django.db import models
from django.core.exceptions import ValidationError

class Post (models.Model):
    id = models.AutoField(primary_key=True)
    json = models.JSONField()


