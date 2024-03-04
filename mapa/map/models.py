from django.db import models

class Post (models.Model):
    json = models.JSONField()

    def __str__(self):
        return self.json
