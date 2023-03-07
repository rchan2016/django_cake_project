from django.db import models


class DataDescription(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()

