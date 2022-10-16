from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import login, logout   , authenticate
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.views.generic import TemplateView, ListView, FormView, View
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import *
from .forms import *



class IndexView(ListView):
    model = PostalItem
    context_object_name = 'items'
    template_name = 'index.html'


class AboutPageView(TemplateView):
    template_name = "about.html"


class SendItemView(FormView):
    template_name = 'send_item.html'
    form_class = PostalItemForm
    success_url = ''

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


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


class LoginView(View):
    
    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        pass
    


class SignUpView(FormView):
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = ''

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


class PostalItemDetail():
    pass


def detail_view(request, pk):
    try:
        item = PostalItem.objects.get(id=pk)
    except PostalItem.DoesNotExist as ex:
        raise Http404('Not found')
    return render(request, 'detail.html', {'item': item})

