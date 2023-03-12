from django.db import models

from chess_inventory.validators import validate_pgn


class Game(models.Model):
    pgn = models.TextField(validators=[validate_pgn])
    description = models.CharField(max_length=100, default='', blank=True)
    event = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    date = models.DateField(null=True)
    round = models.CharField(max_length=20)
    white = models.CharField(max_length=100)
    black = models.CharField(max_length=100)
    result = models.CharField(max_length=10)
    eco = models.CharField(max_length=10, null=True)
    opening = models.CharField(max_length=100, null=True)
    variation = models.CharField(max_length=100, null=True)
    ecot = models.CharField(max_length=10, null=True)
    openingt = models.CharField(max_length=100, null=True)
    variationt = models.CharField(max_length=100, null=True)
