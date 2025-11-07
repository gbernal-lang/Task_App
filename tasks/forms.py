# Se importa forms
from django import forms
 
# import GeeksModel from models.py
from .models import Task
 
# create a ModelForm
class GeeksForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Task
        fields = "__all__"