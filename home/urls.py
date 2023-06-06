from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/',views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('send-email/', views.SendEmailView.as_view(), name='send_email'),
    path('contact/', views.contact, name='contact'),
    path('form/', views.form1_view, name='form1_view'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/<slug:pk>/', views.profileDetails, name='profileDetails'),
    path('logout/', views.logout, name="logout")
]
 