from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import signUpForm, addRecordForm
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


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)  # Fetch the record by primary key
        return render(request, 'record.html', {'customer_record': customer_record}) 
    else:
        messages.error(request, 'You must be login first.')
        return redirect('home')    

def delete_record(request, pk):
        if request.user.is_authenticated:
            delete_record = Record.objects.get(id=pk)  # Fetch the record by primary key
            delete_record.delete()
            messages.error(request, 'Record deleted successfully.')
            return redirect('home')
        else:
            messages.error(request, 'You must be login first.')
            return redirect('home')  
def add_record(request):
    form= addRecordForm(request.POST or None)  # Initialize the form
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                new_record = form.save()
                messages.success(request, 'Record added successfully.')
                return redirect('home')  # Redirect to home after adding the record
        return render(request, 'add_record.html',{'form':form})  # Render the add record form
    else:
        messages.error(request, 'You must be login first.')
        return redirect('home')        
    
def update_record(request, pk):   
    if request.user.is_authenticated: 
        current_record = Record.objects.get(id=pk)  # Fetch the record by primary key 
        form= addRecordForm(request.POST or None, instance=current_record)  # Initialize the form with preocupied value
        if form.is_valid():
            updated_record=form.save()
            print("Saved Record ID:", updated_record.id)
            messages.success(request, 'Record updated successfully.')
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.error(request, 'You must be login first.')
        return redirect('home')

