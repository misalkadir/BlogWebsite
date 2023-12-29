from django.forms import ModelForm, TextInput, Select
from .models import Yazi, Yorum

class yaziEkleForm(ModelForm):
    class Meta:
        model = Yazi

        exclude = ["begeniSayisi", "goruntulenmeSayisi"]

        widgets = {
            'başlık': TextInput(attrs={'class': 'form-control'}),
            'kategori': Select(attrs={'class': 'form-control'}),
        }
