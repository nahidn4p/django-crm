from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    #check to see if the user is authenticated
    if request.method=='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        #authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')  # Redirect to home after successful login
        else:
            messages.error(request, 'There is an error.')
            return redirect('home')
    else:

        return render(request, 'home.html',{})  # Render the home page template

# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')  # Redirect to home after logout

def register_user(request):
    return render(request, 'register.html',{})