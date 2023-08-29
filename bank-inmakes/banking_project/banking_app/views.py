

# Create your views here.
from django.shortcuts import render, redirect
# from django.contrib import messages
# from .models import Customer
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('/login')

    return render(request,'login.html')


def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
                return redirect(".")
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email id already taken')
                return redirect('.')
            else:
               user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)

               user.save()
               return redirect('/login')
        else:
            messages.info(request,'password not matching')
            return redirect('.')


    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')




# added
from django.shortcuts import render
from .forms import PersonForm
from django.http import JsonResponse
from .models import Branch

def person_form(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "Form submitted successfully!"
            return render(request, 'form.html', {'form': form,'success_message': success_message})
           
    else:
        form = PersonForm()
    
    return render(request, 'form.html', {'form': form,})

def get_branches(request):
    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district_id=district_id).values("id", "name")
    return JsonResponse({"branches": list(branches)})
