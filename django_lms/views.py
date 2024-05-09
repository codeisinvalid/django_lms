from django.shortcuts import render, redirect

def BASE(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'main/home.html')

def single_course(request):
    return render(request, 'main/single-course.html')