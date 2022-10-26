from django.conf import settings
from django.db import models

from .baz import Baz


class Bar(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL)
    baz = models.ForeignKey(Baz, on_delete=models.PROTECT)
