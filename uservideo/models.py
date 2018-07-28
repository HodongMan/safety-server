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