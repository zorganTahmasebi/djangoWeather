from django.shortcuts import render

# This is my views in djnago

def home(request):
    return render(request, 'home.html', {})
 

def about(request):
    return render(request, 'about.html', {})