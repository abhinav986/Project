from django.db import models


class Infostrip(models.Model):
    icon = models.CharField(max_length=40)
    title = models.CharField(max_length=70)
    subtitle = models.CharField(max_length=100)

class FooterStrip(models.Model):
    title = models.CharField(max_length=70)
    description = models.CharField(max_length=150)
    url = models.URLField(max_length=255)