from django.db import models

# Create your models here.
class Hash(models.Model):
    text = models.TextField()
    hash = models.CharField(max_length=64)

    def __str__(self):
        return self.text