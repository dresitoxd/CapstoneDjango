from django.db import models
from datetime import timedelta

class Subasta(models.Model):
    image = models.ImageField(upload_to='subastas_imagen/')
    title = models.CharField(max_length=50)
    description = models.TextField()
    game = models.CharField(max_length=100)
    rarity = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)
    duration = models.PositiveIntegerField()  # Duración en horas
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.game}'

    def end_time(self):
        return self.created_at + timedelta(hours=self.duration)

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()
