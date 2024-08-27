from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(UserCreationForm):
    def save(self,commit=True):
        user=super().save(commit=False)
        user.is_superuser = True
        if commit:
            user.save()
        return user