from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import login, logout   , authenticate
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import LoginForm, PostalItemForm, SignUpForm


def index(request):
    try:
        items = PostalItem.objects.all()
    except PostalItem.DoesNotExist:
        items = None
    #return HttpResponse("<h1>Hello, world!</h1>")
    return render(request, 'index.html', context={'items': items})


def about_page(request):
    return render(request, 'about.html')


def send_item(request):
    if request.method == 'POST':
        form = PostalItemForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('index')
    else:
        form = PostalItemForm()
    return render(request, 'send_item.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                HttpResponse('Invalid account')
                #redirect('invalid_acc') TODO
    else:
        form = LoginForm()
    return render(request, 'login_page.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('login')
        else:
            print(form.errors)
            HttpResponse('Invalid form')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def detail_view(request, pk):
    try:
        item = PostalItem.objects.get(id=pk)
    except PostalItem.DoesNotExist as ex:
        raise Http404('Not found')
    return render(request, 'detail.html', {'item': item})

