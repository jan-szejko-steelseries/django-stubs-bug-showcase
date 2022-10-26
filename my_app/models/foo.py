from django.db import models

from .bar import Bar


class Foo(models.Model):
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE)
