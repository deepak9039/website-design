from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return render(request,'home.html')

def aboutus(request):
    return render(request,'aboutus.html')

def our_team(request):
    return render(request, 'our_team.html')

def contact(request):
    return render(request, 'contact.html')