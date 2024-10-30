from django.shortcuts import render, redirect
from .forms import CustomUserLoginForm, UserRegisterForm
from django.contrib.auth import login,logout ,authenticate

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
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.DATA)
        if form.is_valid():
            form.save()
    else:
        form = UserRegisterForm()
    return render(request, 'autentication/register.html', {'form':form})