from django.shortcuts import render, redirect
from django.contrib.auth.forms import  AuthenticationForm

from .forms import SignUpForm

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('/uchwaly')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})