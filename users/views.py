from django.shortcuts import redirect, render
from . forms import *

from django.contrib.auth import authenticate, login, logout

# Create your views here.
def registerUser(request):
    forms = UserRegisterForm()

    if request.method == 'POST':
        forms = UserRegisterForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('login')

    context = {'forms':forms}
    return render(request, 'users/register.html', context)

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('chatroom:room-home')

    context = {}
    return render(request, 'users/login.html', context)   

def logoutUser(request):
    logout(request)
    return redirect('chatroom:room-home')     
