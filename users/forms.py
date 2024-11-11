from django import forms
from .models import Subasta, Puja, Carta

class SubastaForm(forms.ModelForm):
    GAME_CHOICES = [
        ('Mitos y Leyendas', 'Mitos y Leyendas'),
        ('Yu Gi Oh!', 'Yu Gi Oh!'),
        ('Pokemon TCG', 'Pokemon TCG'),
    ]

    DURATION_CHOICES = [(i, f"{i:02d} horas") for i in range(1, 25)]

    RAREZA_CHOICES = [
        ('Normal', 'Normal'),
        ('Real', 'Real'),
        ('Ultra real', 'Ultra real'),
        ('Mega Real', 'Mega Real'),
        ('Legendaria', 'Legendaria'),
    ]

    CONDICION_CHOICES = [
        ('Nueva', 'Nueva'),
        ('Seminueva', 'Seminueva'),
        ('Usada', 'Usada'),
    ]

    game = forms.ChoiceField(choices=GAME_CHOICES)
    duration = forms.ChoiceField(choices=DURATION_CHOICES)
    rareza = forms.ChoiceField(choices=RAREZA_CHOICES)
    condicion = forms.ChoiceField(choices=CONDICION_CHOICES)

    class Meta:
        model = Subasta
        fields = ['image', 'title', 'description', 'game', 'rareza', 'condicion', 'duration']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class PujaForm(forms.ModelForm):
    class Meta:
        model = Puja
        fields = ['amount']
        widgets = {
            'amount': forms.NumberInput(attrs={'min': 0, 'step': '0.01'})
        }

class CartaForm(forms.ModelForm):
    GAME_CHOICES = [
        ('Mitos y Leyendas', 'Mitos y Leyendas'),
        ('Yu Gi Oh!', 'Yu Gi Oh!'),
        ('Pokemon TCG', 'Pokemon TCG'),
    ]

    RAREZA_CHOICES = [
        ('Normal', 'Normal'),
        ('Real', 'Real'),
        ('Ultra real', 'Ultra real'),
        ('Mega Real', 'Mega Real'),
        ('Legendaria', 'Legendaria'),
    ]

    CONDICION_CHOICES = [
        ('Nueva', 'Nueva'),
        ('Seminueva', 'Seminueva'),
        ('Usada', 'Usada'),
    ]

    game = forms.ChoiceField(choices=GAME_CHOICES)
    rareza = forms.ChoiceField(choices=RAREZA_CHOICES)
    condicion = forms.ChoiceField(choices=CONDICION_CHOICES)

    class Meta:
        model = Carta
        fields = ['image', 'title', 'description', 'game', 'rareza', 'condicion', 'price']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
