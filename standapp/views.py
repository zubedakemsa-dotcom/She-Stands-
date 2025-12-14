
from django.shortcuts import render, redirect
from .models import Resource, Mentor, Story, ContactMessage

def home(request):
    resources = Resource.objects.all()
    mentors = Mentor.objects.all()
    stories = Story.objects.all()
    return render(request, 'index.html', {
        'resources': resources,
        'mentors': mentors,
        'stories': stories
    })

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        ContactMessage.objects.create(name=name, email=email, message=message)
        return redirect('home')
    return redirect('home')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages





def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')


@login_required
def profile(request):
    return render(request, 'profile.html')


def logout_view(request):
    logout(request)
    return redirect('login')

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


    
def home(request):
    return render(request, 'standapp/index.html')


def login_view(request):
    return render(request, 'standapp/login.html')


@login_required
def profile(request):
    return render(request, 'standapp/profile.html')


    return render(request, 'profile.html')
