from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Case


class Game(models.Model):

    name = models.CharField(max_length=100)
    game_type = models.ForeignKey("GameType", on_delete=CASCADE)
    description = models.CharField(max_length=150)
    number_of_players = models.IntegerField()
    gamer = models.ForeignKey("Gamer", on_delete=CASCADE)
    maker = models.CharField(max_length=50)
    skill_level = models.IntegerField()