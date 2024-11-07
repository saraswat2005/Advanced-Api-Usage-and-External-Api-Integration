from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        profession = request.POST['profession']
        
        if profession.lower() == 'lawyer':
            is_lawyer = True
        else:
            is_lawyer = False 
        print('here')
        user = User.objects.create_user(first_name=first_name, email=email, password=password)
        user.save()
        return redirect('chat')
    return render(request, 'signup.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = authenticate(request, email=email, password=password)
        except:
            return redirect('chat')
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully.')
            return redirect('chat')
        else:
            messages.error(request, 'Invalid email or password.')
            return redirect('login')

    return render(request, 'login.html')
