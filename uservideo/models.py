from django.db import models
from amo.models import ModelBase


class UserVideo(ModelBase):

    user = models.CharField(max_length=255)
    video_id = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField(default=0)
    favorite = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = 'UserVideo'
        ordering = ('favorite', '-created',)

class Video(ModelBase):

    video_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    thumbnails = models.URLField(max_length=255, blank=True)
    publishedAt = models.DateTimeField()

    class Meta:
        db_table = 'Video'
        ordering = ('-created',)