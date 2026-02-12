from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['title', 'brand', 'model_name', 'year', 'price', 'transmission', 'mileage', 'image', 'description']
        # Tailwind стилдерин кошуу үчүн:
        widgets = {
            field: forms.TextInput(attrs={'class': 'w-full p-4 bg-slate-800 rounded-xl border border-slate-700 outline-none focus:border-blue-500 text-white mb-4'})
            for field in ['title', 'brand', 'model_name', 'year', 'price', 'mileage']
        }