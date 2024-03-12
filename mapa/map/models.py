from django.db import models

class Post (models.Model):
    id = models.AutoField(primary_key=True)
    json = models.JSONField()


