# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render,redirect
from .forms import LoginForm,RegisterForm, PestQuery
from django.contrib.auth import authenticate,login,get_user_model


# Create your views here.


def HomePage(request):
    user = request.user
    #farms = Farm.objects.filter(owner=user)
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        password = form.cleaned_data["password"]
        name = form.cleaned_data["name"]
        phoneNo = form.cleaned_data["phoneNo"]
        email = form.cleaned_data["email"]
        User.objects.create_user(password=password, name=name, email=email, phoneNo=phoneNo)
        return redirect("/login")

    return render(request,"index.html",{"form": form,})

def DashboardPage(request):
    user = request.user
    farms = Farm.objects.filter(owner=user)



    return render(request,"home.html",{"farms":farms})


def LoginPage(request):

    form = LoginForm(request.POST or None)
    context = {
        "form": form,
    }
    if form.is_valid():
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            # context['form']=LoginForm()

            return redirect("/dashboard")
        else:
            context['error'] = 'Username or password incorrect'

    return render(request, "login.html", context)

User = get_user_model()


def RegisterPage(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        password = form.cleaned_data["password"]
        name = form.cleaned_data["name"]
        phoneNo = form.cleaned_data["phoneNo"]
        email = form.cleaned_data["email"]
        User.objects.create_user(password =password, name=name, email=email, phoneNo=phoneNo )
        return redirect("/login")
    context = {
            "form": form,
    }
    return render(request, "auth/register.html", context)


def PestsPage(request):
    form = PestQuery(request.POST or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.farmer = request.user
        #form.pest = model.output
        #form.accuracy = model.output
        form.save()
        return redirect("/results")
    context = {
            "form": form,
    }
    return render(request, "query.html", context)