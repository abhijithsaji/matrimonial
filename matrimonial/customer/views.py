from django.db.models import base
from django.shortcuts import render ,redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from django.http import HttpResponse
from django.http import JsonResponse

from datetime import timedelta
import online_users.models

from .forms import *
# Create your views here.

@login_required
def home(request):
    
    # user_activity_objects = online_users.models.OnlineUserActivity.get_user_activities(timedelta(minutes=5))
    # number_of_active_users = user_activity_objects.count()  
    # users = (user for user in  user_activity_objects)
    # print(users)
    # for user in users:
    #     print(user.user.email)
    #     if user.user ==  request.user:
    #         print("online.................")
    user = request.user
    customers = Customer.objects.exclude(user = user)


    context = {
        'customers':customers,
        
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



def edit_profile_basic(request):
    
    customer = request.user.customer
    form = CustomerBasicForm(instance = customer)
    basic = True

    if request.method == "POST":
        form = CustomerBasicForm(request.POST, instance = customer)
        try:
            religion = request.POST.get('religion')
            religion = Religion.objects.get(name=religion)

            caste = request.POST.get('caste')
            caste = Caste.objects.get(name=caste , religion=religion)

        except:
            messages.warning(request, 'Please enter religion/cast details properly')
            return redirect('edit-profile-basic')
            

        if form.is_valid():
            form.save()
            customer.religion = religion
            customer.caste = caste
            customer.save()
            messages.warning(request, 'Please make sure the details entered is valid')  
            return redirect('edit-profile-personal')

        
    context = {
        'form':form,
        'basic':basic,
    }
    return render(request, 'customer/edit_profile_basic.html',context)


def edit_profile_personal(request):
    
    customer = request.user.customer
    form = CustomerPersonalForm(instance = customer)
    personal = True

    if request.method == "POST":
        form = CustomerPersonalForm(request.POST, instance = customer)       
        
        if form.is_valid():
            form.save()

            return redirect('edit-profile-personality')

        
    context = {
        'form':form,
        'personal':personal,
    }
    return render(request, 'customer/edit_profile_personal.html',context)


def edit_profile_personality(request):
    
    customer = request.user.customer
    form = CustomerPersonalityForm(instance = customer)
    form2 = MultiForm(instance = customer)
    personality = True

    if request.method == "POST":
        form = CustomerPersonalityForm(request.POST, instance = customer)  
        form2 = MultiForm(request.POST,instance = customer)


        if form.is_valid():
            form.save()
        
        if form2.is_valid():
            music = request.POST.get('music')
            music_types = form2.cleaned_data['music_types']
            print(music_types.exists())
            reading = request.POST.get('reading')
            reading_types = form2.cleaned_data['reading_types']
            sports = request.POST.get('sports')
            sport_types = form2.cleaned_data['sport_types']
            foods = request.POST.get('foods')
            food_types = form2.cleaned_data['food_types']
            dress = request.POST.get('dress')
            dress_types = form2.cleaned_data['dress_types']
            movie = request.POST.get('movie')
            movie_types = form2.cleaned_data['movie_types']


            customer.music = music
            if music_types.exists():
                customer.music_types.set(music_types)
            
            customer.reading = reading
            if reading_types.exists():
                customer.reading_types.set(reading_types)

            customer.sports = sports
            if sport_types.exists():
                customer.sport_types.set(sport_types)

            customer.foods = foods
            if food_types.exists():
                customer.food_type.set(food_types)

            customer.dress = dress
            if dress_types.exists():
                customer.dress_types.set(dress_types)

            customer.movie = movie
            if movie_types.exists():
                customer.movie_types.set(movie_types)
            customer.save()

        

            return redirect('edit-profile-astro')

        
    context = {
        'form':form,
        'form2':form2,
        'customer':customer,
        'personality':personality,
    }
    return render(request, 'customer/edit_profile_personality.html',context)



def edit_profile_astro(request):
    
    customer = request.user.customer
    form = CustomerAstroForm(instance = customer)
    astro = True

    if request.method == "POST":
        form = CustomerAstroForm(request.POST, instance = customer)       
        
        if form.is_valid():
            form.save()

            return redirect('home')

        
    context = {
        'form':form,
        'astro':astro,
    }
    return render(request, 'customer/edit_profile_astro.html',context)



def edit_profile_prefered_partner(request):
    
    customer = request.user.customer
    form = MultiForm(instance = customer)
    prefered_partner = True

    if request.method == "POST":
        print(request.POST)
        form = MultiForm(request.POST, instance = customer)       
        # if form.is_valid():
        #     form.save()   
        
    context = {
        'form':form,
        'prefered_partner':prefered_partner,
    }
    return render(request, 'customer/edit_profile_prefered_partner.html',context)


def get_json_religion_data(request):
    qs_val = list(Religion.objects.values())
    return JsonResponse({'data':qs_val})

def get_json_caste_data(request, *args, **kwargs):
    selected_religion = kwargs.get('religion')
    print(kwargs.get('caste'))
    obj_caste = list(Caste.objects.filter(religion__name=selected_religion).values())
    return JsonResponse({'data':obj_caste}) 


# Profile Details


def my_profile(request):
    customer = request.user.customer
    context = {
        'customer':customer,
    }
    return render(request, 'customer/my_profile.html',context)