from django.db import models


class BazQuerySet(models.QuerySet):
    pass


BazManager = models.Manager.from_queryset(BazQuerySet)


class Baz(models.Model):
    objects = BazManager()
