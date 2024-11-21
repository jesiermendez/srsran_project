from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import CustomUser

# Create your forms here.
class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}))


class UserRegisterForm(UserCreationForm):
   
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email','is_staff', 'is_superuser', 'phone', 'picture', 'dni')
        labels = {
            'username':'Nombre de usuario', 'first_name':'Nombre', 'last_name':'Apellidos', 'email':'Correo electronico',
            'is_staff':'Acceso al panel de administracion', 'is_superuser':'Super usuario',
            'phone':'Telefono', 'picture':'Foto', 'dni':'Carnet de identidad'
        }
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exclude(id=self.instance.id).exists():
            raise forms.ValidationError('El nombre de usuario ya esta en uso')
        return username
    
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone', 'picture', 'dni')