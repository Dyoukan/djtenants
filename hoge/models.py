from typing import Reversible
from django.db import models
from django.db.models.fields import reverse_related

class Hoge(models.Model):
    
    name = models.CharField('名前', max_length=50)
    rank = models.IntegerField("ランク")


