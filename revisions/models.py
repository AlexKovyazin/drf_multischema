from django.db import models
from django.contrib.postgres.fields import ArrayField

SCHEMA_CHOICES = [(1, 'день'), (2, 'ночь')]


class Revision(models.Model):
    shop = models.ForeignKey(
        'base_models.Shop',
        related_name='revisions',
        on_delete=models.DO_NOTHING
    )
    rev_date = models.DateField()
    schema = models.CharField(choices=SCHEMA_CHOICES)
    status = models.IntegerField()


class WorkSpace(models.Model):
    name = models.CharField()
    allowed_ranks = ArrayField(
        models.IntegerField()
    )
