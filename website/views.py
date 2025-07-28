from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import signUpForm
from .models import Record
# Create your views here.
def home(request):
    records = Record.objects.all()  # Fetch all records from the database
    
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

        return render(request, 'home.html',{'records':records})  # Render the home page template

# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')  # Redirect to home after logout

def register_user(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            #Authenticate and log in the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')   
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You are now logged in.')
            else:
                messages.error(request, 'There was an error logging you in.')
            return redirect('home')  # Redirect to home after successful registration
        else:
            messages.error(request, 'There was an error with your registration.')
    else:
        form = signUpForm()
        return render(request, 'register.html',{'form': form})  # Render the registration form
    return render(request, 'register.html',{'form': form})  # Render the registration form    