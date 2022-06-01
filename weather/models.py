import uuid  # generate unique id
from django.db import models


class Sensor(models.Model):
    sensor_id = models.UUIDField(primary_key=True,
                                 default=uuid.uuid4, editable=False)
    city_name = models.CharField(max_length=32, null=False)
    country = models.CharField(max_length=32, null=False)

    def __init__(self, sensor_id, country, city_name):
        self.sensor_id = sensor_id
        self.country = country
        self.city_name = city_name

    def __str__(self):
        return str(self.sensor_id)