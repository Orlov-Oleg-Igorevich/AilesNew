from django.shortcuts import render, get_object_or_404, redirect
from .models import PersonInfo
from .forms import PersonForm


def handle_uploaded_file(f):
    name, fmt = f.name.split('.')
    cnt = 0
    try:
        while True:
            with open(f'uploads/{name}{"" if cnt == 0 else f"({cnt})"}.{fmt}', 'rb') as _:
                cnt += 1
    except:
        with open(f'uploads/{name}{"" if cnt == 0 else f"({cnt})"}.{fmt}', 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)


def index(request):
    return render(request, "Social_networks/index.html")


def action_page(request):
    return render(request, "Social_networks/signup.html")


def about(request):
    users = PersonInfo.objects.all()
    data = {
        'users': users,
    }
    return render(request, "Social_networks/about.html", context=data)


def contact(request):
    return render(request, "Social_networks/contact.html")


def news(request):
    return render(request, "Social_networks/News.html")


def signup(request):
    if request.method == "POST":
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            PersonInfo.objects.create(**form.cleaned_data)
            return redirect('main-page')
    else:
        form = PersonForm()
    data = {
        'form': form,
    }
    return render(request, "Social_networks/signup.html", data)


def show_user(request, user_slug):
    user_info = get_object_or_404(PersonInfo, slug=user_slug)
    data = {
        'user': user_info,
    }
    return render(request, "Social_networks/Profile.html", data)


def user_friends(request, user_slug):
    return render(request, 'Social_networks/Друзья.html')

