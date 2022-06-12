from django import forms
from .models import Reserv


class Reservform(forms.ModelForm):
    class Meta:
        model = Reserv
        fields = "__all__"
        