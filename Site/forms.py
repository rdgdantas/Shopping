from django import forms
from Site.models import Cliente

class ClientForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'