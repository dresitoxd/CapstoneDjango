from django import forms
from .models import Subasta

class SubastaForm(forms.ModelForm):
    class Meta:
        model = Subasta
        fields = ['image', 'title', 'description', 'game', 'rarity', 'condition', 'duration']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'duration': forms.NumberInput(attrs={'min': 1}),
        }
