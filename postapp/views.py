from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
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

    def get_context_data(self, *args, **kwargs):
        context = super(SendItemView, self).get_context_data(*args, **kwargs)
        try:
            print(Customer.objects.filter(user=self.request.user))      
            context['customer'] = Customer.objects.filter(user=self.request.user)
        except Customer.DoesNotExist:
            context['customer'] = None
        return context

    def form_valid(self, form):
        item = form.save(commit=False)
        item.sender = Customer.objects.get(user=self.request.user)
        item.save()
        return super().form_valid(form)


class AddCustomer(FormView):
    template_name = 'become_a_customer.html'
    form_class = CustomerForm
    success_url = 'send'

    def form_valid(self, form):
        customer = form.save(commit=False)
        customer.user = self.request.user
        customer.save()
        return super().form_valid(form)


class LoginView(View):
    form_class = LoginForm
    template_name = 'login_page.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                HttpResponse('Invalid account')
        return render(request, self.template_name, {'form': form})
    

class SignUpView(FormView):
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = 'index'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


class PostalItemDetail(View):
    template_name = 'detail.html'
    
    def get(self, request, pk, *args, **kwargs):
        return render(request, self.template_name, 
        {'item': get_object_or_404(PostalItem, pk=pk)})