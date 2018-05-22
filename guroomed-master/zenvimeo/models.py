from django.db import models
from embed_video.fields import EmbedVideoField
# from django.utils.encoding import python_2_unicode_compatible
# from django.utils import timezone
# import datetime
from django.contrib.auth.models import Group
import vimeo
# from django.conf import settings

class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    video = EmbedVideoField()  # same like models.URLField()
    video_group = models.ForeignKey(Group, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    class Meta:
        permissions = (
            ("view_videos_ui", "Can view Videos in website"),
        )