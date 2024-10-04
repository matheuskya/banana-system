from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from main.models import Profile


# Create your views here.
@login_required()
def index(request):
    context = {}
    return render(request, "main/index.html", context)

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})

def logout(request):
    return render(request, "registration/logout.html")

def view_profile(request):
    profile = Profile.objects.get(user=request.user)
    image_url = profile.profile_picture.url
    context = {
        'profile' : profile,
        'profile_picture' : image_url
    }
    print(image_url)
    return render(request, "main/profile.html", context)

def edit_profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance = request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('view_profile')
    else:
        user_form = UserUpdateForm(instance = request.user)
        profile_form = ProfileUpdateForm(instance = request.user)
    context = {
        'user_form' : user_form,
        'profile_form' : profile_form
    }
    return render(request, 'main/edit_profile.html', context)

def chat_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('login')
    context = {}
    return render(request, 'main/chat.html', context)
