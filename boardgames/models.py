from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from .choices import DIFFICULTY_CHOICES, RANDOMNESS_CHOICES, GAME_GENRE_CHOICES


class Game(models.Model):
    name = models.CharField(max_length=50)
    max_players_count = models.IntegerField(
        validators=[MinValueValidator(limit_value=2)], default=2
    )
    age_restriction = models.IntegerField(
        validators=[MinValueValidator(limit_value=7)], default=7
    )
    difficulty = models.IntegerField(choices=DIFFICULTY_CHOICES, default=1)
    rng_factor = models.IntegerField(choices=RANDOMNESS_CHOICES, default=1)
    genre = models.IntegerField(choices=GAME_GENRE_CHOICES, default=1)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("game-detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    game = models.ForeignKey(
        "boardgames.Game", on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    context = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
