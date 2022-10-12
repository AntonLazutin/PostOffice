from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about_page, name='about'),
    path('send', views.send_item, name='send'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('signup', views.signup_view, name='signup'),
    path('detail/<int:pk>', views.detail_view, name="detail"),
]
