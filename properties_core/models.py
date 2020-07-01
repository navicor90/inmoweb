from django.db import models
from django.db.backends.mysql.base import DatabaseWrapper
DatabaseWrapper.data_types['DateTimeField'] = 'datetime' # fix for MySQL 5.5


class Property(models.Model):
    PROPERTY_TYPES = [('HO', 'House'),
                      ('AP', 'Apartment'),
                      ('FI', 'Field')]

    ref_id = models.CharField(max_length=100)
    district = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    currency = models.CharField(max_length=3)
    amount = models.FloatField()
    price = models.CharField(max_length=20)
    url = models.CharField(max_length=500)
    source_web = models.CharField(max_length=50)
    scrapped_date = models.DateField()
    last_push = models.DateTimeField(auto_now=True)
    description = models.TextField()
    extra_json_info = models.TextField()
    property_type = models.CharField(max_length=2, choices=PROPERTY_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

