from django.db import models


class InfoPost(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    date_created = models.DateTimeField(auto_now_add=True)
