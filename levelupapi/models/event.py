from django.db import models


class Event(models.Model):

    host = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    date = models.IntegerField(max_length=50)
    time = models.TimeField()
    description = models.TextField()
    title = models.CharField(max_length=100)
    attendees = models.ManyToManyField("Gamer", through="EventGamer", related_name="attending")
