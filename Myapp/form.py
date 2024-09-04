from django import forms
from Myapp.models import User

class User_form(forms.ModelForm):
    class Meta():
        model=User
        fields='__all__'