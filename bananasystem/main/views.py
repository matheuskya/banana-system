from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.forms import RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login/')
def index(request):
    context = {}
    return render(request, "main/index.html", context)

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})
