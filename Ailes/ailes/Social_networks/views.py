from django.shortcuts import render, get_object_or_404
from .models import PersonInfo

# Create your views here.
def index(request):
    return render(request, "Social_networks/index.html")

def action_page(request):
    return render(request, "Social_networks/signup.html")

def about(request):
    return render(request, "Social_networks/about.html")

def contact(request):
    return render(request, "Social_networks/contact.html")

def News(request):
    return render(request, "Social_networks/News.html")

def signup(request):
    return render(request, "Social_networks/signup.html")

def show_user(request, user_slug):
    user = get_object_or_404(PersonInfo, slug=user_slug)

    data = {

    }

    return render(request, "Social_networks/signup.html", data)