from django.db import models

class Pokemon(models.Model):
    pokemon_name = models.CharField(max_length=30)
    base_experience = models.IntegerField()
    pokemon_type = models.CharField(max_length=30)
    weight = models.IntegerField()
