from django.db import models
from amo.models import ModelBase

class VideoInteraction(ModelBase): #

    video_id = models.CharField(max_length=255)
    pointed_time = models.FloatField(default=0)


    class Meta:
        db_table = 'VideoInteraction'
        ordering = ('-created',)


class VideoHightlight(ModelBase):

    video_id = models.CharField(max_length=255)
    start_time = models.FloatField()
    end_time = models.FloatField()

    class Meta:
        db_table = 'VideoHightlight'
        ordering = ('-created',)
    


