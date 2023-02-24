from django import forms
from .models import userdata

class userdataform(forms.ModelForm):
    class Meta:
        model = userdata
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mob_no': forms.TextInput(attrs={'class': 'form-control'}),
            # 'mob_no': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'min': '0', 'max': '9999999999'}),

        }
