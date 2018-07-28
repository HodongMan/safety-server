from django.db import models
from amo.models import ModelBase


class CommentHighlight(ModelBase):

    video_id = models.CharField(max_length=255)
    highlight_time = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'CommentHighlight'
        ordering = ('-created',) 