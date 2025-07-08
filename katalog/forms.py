from django import forms
from .models import Kopi

class KopiForm(forms.ModelForm):
    class Meta:
        model = Kopi
        fields = '__all__'
