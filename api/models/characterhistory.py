from django.db import models


class CharacterHistory(models.Model):
    created           = models.DateTimeField(auto_now_add=True)
    character         = models.ForeignKey('api.Character', related_name='history')
    x                 = models.FloatField()
    y                 = models.FloatField()
    z                 = models.FloatField()
