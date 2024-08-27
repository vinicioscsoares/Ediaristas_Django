from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuarioForm(UserCreationForm):
    
    email=forms.EmailField(required=False)
    
    class Meta:
        model= User
        fields={"username","email","password1","password2"}
        
    def save(self,commit=True):
        user=super().save(commit=False)
        user.email=self.cleaned_data['email']
        user.is_superuser = True
        if commit:
            user.save()
        return user