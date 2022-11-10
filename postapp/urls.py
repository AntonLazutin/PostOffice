from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about', views.AboutPageView.as_view(), name='about'),
    path('send', views.SendItemView.as_view(), name='send'),
    path('join_service', login_required(views.AddCustomer.as_view(), login_url='login'), name='join'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LoginView.as_view(), name='logout'),
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('detail/<int:pk>', views.PostalItemDetail.as_view(), name="detail"),
]
