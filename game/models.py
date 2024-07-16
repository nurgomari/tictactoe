from django.db import models

# Create your models here.

class Game(models.Model):
    player_x = models.CharField(max_length=50)
    player_o = models.CharField(max_length=50)
    board = models.CharField(max_length=9, default="---------")
    current_turn = models.CharField(max_length=1, default="X")
    winner = models.CharField(max_length=1, blank=True, null=True)  

    def __str__(self):
        return f"Juego {self.id} - {self.player_x} vs {self.player_o}"
