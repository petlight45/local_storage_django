from django.shortcuts import render, redirect


def signin(request):
    return render(request, 'user/login.html')


def signup(request):
    return render(request, 'user/signup.html')


def home(request):
    return render(request, 'user/index.html')
