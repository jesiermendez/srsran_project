from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserLoginForm, UserRegisterForm, CustomUserChangeForm
from django.contrib.auth import login,logout ,authenticate
from .models import CustomUser


# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])        
            if user is not None:
                login(request, user)
                return redirect('api_view')
    else:
        form = CustomUserLoginForm()       
    return render(request, 'autentication/auth.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    mensaje = ''
    users = CustomUser.objects.all()
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                mensaje = 'Usuario creado satisfactoriamente'
        else:
            form = UserRegisterForm()
    else:
        return redirect('login')
    
    return render(request, 'autentication/register.html', {'form':form,'users':users ,'mensaje':mensaje})

def delete_user(request, user_id):
    if request.user.is_authenticated:
        user = get_object_or_404(CustomUser, id=user_id)
        user.delete()
    else:
        return redirect('login')
    return redirect('register')

def user_edit(request, user_id):
    usuario = get_object_or_404(CustomUser, id=user_id)
    mensaje = ''    
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserChangeForm(request.POST, request.FILES, instance= usuario)
            if form.is_valid():
                form.save()
                return redirect('register')
        else:
            form = CustomUserChangeForm(instance=usuario)
    else:
        return redirect('login')
     
    return render(request, 'autentication/user_edit.html', {'form':form, 'user1': usuario, 'mensaje':mensaje})