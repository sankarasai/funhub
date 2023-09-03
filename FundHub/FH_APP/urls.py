from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('Homepage',views.homepage,name='homepage'),
    path('Pricing',views.pricing,name='pricing'),
    path('login_page',views.login_page,name='login_page'),
    path('login_check',views.login_check,name='login_check'),
    path('signup_view',views.signup_view,name='signup_view'),
    path('logout_view',views.logout_view,name='logout_view'),
    path('create_content',views.create_content,name='create_content'),
    path('watch_content',views.watch_content,name='watch_content'),
]
