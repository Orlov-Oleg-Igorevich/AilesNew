from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "Social_networks/index.html")

def about(request):
    return render(request, "Social_networks/about.html")

def contact(request):
    return render(request, "Social_networks/contact.html")

def News(request):
    return render(request, "Social_networks/News.html")

def signup(request):
    return render(request, "Social_networks/signup.html")