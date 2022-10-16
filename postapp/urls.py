from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about', views.AboutPageView.as_view(), name='about'),
    path('send', views.SendItemView.as_view(), name='send'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('detail/<int:pk>', views.detail_view, name="detail"),
]
