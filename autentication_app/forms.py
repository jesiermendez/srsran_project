from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser

# Create your forms here.
class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}))


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_staff', 'is_superuser', 'phone', 'picture', 'dni')
        labels = {
            'username':'Nombre de usuario', 'first_name':'Nombre', 'last_name':'Apellidos', 'email':'Correo electronico',
            'password1':'Contrasenna', 'password2':'Confirmar contrasenna', 'is_staff':'Acceso al panel de administracion', 'is_superuser':'Super usuario',
            'phone':'Telefono', 'picture':'Foto', 'dni':'Carnet de identidad'
        }
