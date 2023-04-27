from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

class VRegister(View):

    def get(self, request):
        form = UserCreationForm()
        return render(request, "register/register.html", {"form":form})

    def post(self,request):
        
        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()
            login(request, user)

            return redirect('Home')

        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

                return render(request, "register/register.html", {"form":form})

def close_session(request):
    logout(request)
    return redirect('Home')

def open_session(request):

    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            name_user = form.cleaned_data.get("username")
            passw_user = form.cleaned_data.get("password")
            user = authenticate(username = name_user, password = passw_user)
            if user is not  None:
                login(request, user)
                return redirect('Home')
            else:
                messages.error(request, "User no valid")
        else:
            messages.error(request, "Information is wrong")

    form = AuthenticationForm()
    return render(request, "login/login.html",{"form":form})
