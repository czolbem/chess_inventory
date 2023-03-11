from django.db import models


class Game(models.Model):
    pgn = models.TextField()
    description = models.CharField(max_length=100, default='', blank=True)
