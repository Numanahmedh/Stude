import json
import requests
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from blog.models import BlogPost
from .models import StudentUser


def loginview(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username_r = request.POST.get('username')
            password_r = request.POST.get('password')

            user = authenticate(request, username=username_r, password=password_r)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username/Password entered is invalid.')
                return redirect('login')

        return render(request, 'login.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            fullname_r = request.POST.get('fullname')
            date_of_birth_r = request.POST.get('dob')
            degree_r = request.POST.get('degree')
            year_sem_r = request.POST.get('year_sem')
            college_name_r = request.POST.get('college')
            email_r = request.POST.get('email')
            username_r = request.POST.get('username')
            password1_r = request.POST.get('password1')
            password2_r = request.POST.get('password2')

            if password1_r == password2_r:
                if StudentUser.objects.filter(username=username_r).exists():
                    messages.info(request, 'User name is already taken!')
                    return redirect('register')

                elif StudentUser.objects.filter(email=email_r).exists():
                    messages.info(request, 'An account already exists with this email!')
                    return redirect('register')

                else:
                    user_info = StudentUser(fullname=fullname_r, date_of_birth=date_of_birth_r, degree=degree_r,
                                            year_sem=year_sem_r, college_name=college_name_r, username=username_r,
                                            email=email_r, password=password1_r, )
                    user_info.set_password(password1_r)
                    user_info.save()
                    messages.info(request, 'Account successfully created!')
                    return redirect('register')
            else:
                messages.info(request, 'Passwords not matching!')
                return redirect('register')

        return render(request, 'register.html')


@login_required(login_url='login')
def home(request):
    main_url = requests.get(
        "http://newsapi.org/v2/everything?q=Engineering%india&from=2021-01-01&sortBy=publishedAt &apiKey=fbf05bee2a244914b856feac7e1c8a41")
    api = json.loads(main_url.content)

    objects = BlogPost.objects.raw("SELECT * FROM blog_blogpost ORDER BY id DESC LIMIT 3;")

    context = {
        'news': api,
        'posts': objects,
    }

    return render(request, 'index.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')
