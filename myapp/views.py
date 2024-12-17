from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Make sure this line is indented properly


def login(request):
    return render(request, 'login.html')  # Make sure this line is indented properly


def signup(request):
    return render(request, 'signup.html')  # Make sure this line is indented properly

def about(request):
    return render(request, 'about.html')