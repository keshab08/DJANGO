 

# Create your views here.
 

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


from .models import Destination
 

def news(request):
   return render(request, 'news.html', )

def about(request):
   return render(request, 'about.html', )


 

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        # # Check if the passwords match
        # if password1 == password2:
        #     # Check if the username is already taken
        #     if User.objects.filter(username=username).exists():
        #         messages.error(request, "Username already exists")
        #     elif User.objects.filter(email=email).exists():
        #         messages.error(request, "Email already registered")
        #     else:
        #         # Create user
        user = User.objects.create_user(username=username,
                                                password=password1,
                                                email=email,
                                                first_name=first_name,
                                                last_name=last_name)
        user.save()
        print('user created')
        return redirect('/')

        #         messages.success(request, "User registered successfully")
        #         return redirect('index')  # Redirect to a page after registration
        # else:
        #     messages.error(request, "Passwords do not match")
    else:
        return render(request, 'register.html')



def index(request):
   dests=Destination.objects.all()

   return render(request, 'index.html', {'dests':dests})

def login(request):
       
    if request.method=='POST':
        
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username, password=password, )
        
        if user is not None:
         auth.login(request, user)
         return redirect('/')
         
           

    else:
        return render(request, 'login.html',)
    
def logout(request):
    auth.logout(request)
    return redirect('/')
