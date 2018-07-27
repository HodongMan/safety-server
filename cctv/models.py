from django.db import models
from amo.models import ModelBase

class CCTV(ModelBase): #

    management_agency = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255)
    installation_purpose = models.PositiveSmallIntegerField(null=True)
    camera_count = models.PositiveSmallIntegerField(default=1)
    camera_pixel = models.PositiveIntegerField(default=10)
    shooting_direction = models.CharField(max_length=255, default="")
    keep_days = models.PositiveSmallIntegerField(default=10)
    installation_date = models.DateField(null=True)
    latitude = models.DecimalField(max_digits=7, decimal_places=7)
    longitude = models.DecimalField(max_digits=7, decimal_places=7)
    base_date = models.DateField(null=True)

    class Meta:
        db_table = 'CCTV'
        ordering = ('-created',)

    


