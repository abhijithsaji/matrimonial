from django.shortcuts import render ,redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .forms import *
# Create your views here.

@login_required
def home(request):
    r = range(0,10)
    context = {
        'r':r,
    }
    return render(request, 'customer/index.html',context)


def loginpage(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
            try:    
                user = authenticate(request,username=cd['username'],
                password=cd['password'])

            except:
                messages.info(request, 'Username OR password is incorrect')
                
            if user is not None:

                login(request, user)
                
                
                return redirect('home')
                
            else:
                messages.info(request, 'Username OR password is incorrect')
                return redirect('login')
       
    else:
        form = LoginForm()
        
        return render(request, "customer/login.html",{'form':form,})

def register(request): 

    form = CreateUserForm()
    form2 = CustomerForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            group =  Group.objects.get(name='customer')
            user.groups.add(group)

            customer = Customer.objects.create(user=user,uname=username,email=email)
            form2 = CustomerForm(request.POST, instance=customer)
            if form2.is_valid():
                form2.save()

            if user is not None:

                login(request, user)
                
                
                return redirect('home')
            
            else:


                messages.success(request, 'Account was created for ' + username)

                return redirect('login')

    context = {
        'form':form,
        'form2':form2,
        }
    return render(request, 'customer/register.html',context)