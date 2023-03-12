from django.db import models

from chess_inventory.validators import validate_pgn


class Game(models.Model):
    pgn = models.TextField(validators=[validate_pgn])
    description = models.CharField(max_length=100, default='', blank=True)
