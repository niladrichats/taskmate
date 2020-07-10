from django.shortcuts import render, redirect
from .forms import CustomRegisterForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == "POST":
        user_register = CustomRegisterForm(request.POST)
        if user_register.is_valid():
            user_register.save()
            messages.success(request, ("New User Account Created!!"))
            return redirect('register')

    else:
        user_register = CustomRegisterForm()
    return render(request, 'register.html', {'user_register':user_register})
