from django.shortcuts import render, redirect
from .forms import CustomUserLoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout

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
