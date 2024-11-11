from django.db import models
from datetime import timedelta
from django.contrib.auth.models import User

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
    estado = models.CharField(max_length=20, default='Activa')

    def __str__(self):
        return f'{self.title} - {self.game}'

    def end_time(self):
        # Devuelve la fecha y hora final calculada con la duración
        return self.created_at + timedelta(hours=self.duration)

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()


class Puja(models.Model):
    subasta = models.ForeignKey(Subasta, on_delete=models.CASCADE, related_name="pujas")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Monto de la puja
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Puja de {self.user.username} por {self.amount} en la subasta {self.subasta.title}"
    
class Carta(models.Model):
    image = models.ImageField(upload_to='cartas_imagen/')
    title = models.CharField(max_length=50)
    description = models.TextField()
    game = models.CharField(max_length=100)
    rarity = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=0)  # Precio de la carta

    def __str__(self):
        return f'{self.title} - {self.game}'
    
class Carrito(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carrito de {self.user.username}"

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    carta = models.ForeignKey(Carta, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.carta.title}"

    @property
    def total(self):
        return self.carta.price * self.cantidad