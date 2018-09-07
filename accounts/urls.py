# New Method
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.DashbordUser, name="DashbordUser"),
    path('logoutUser/', views.LogoutUser, name="logout"),
    path('login/', views.LoginView, name="login"),
    path('authentification/', views.Authentification, name="authentification"),
    path('inscription/', views.InscriptionView.as_view(), name="Inscription"),
    
    #path('inscription/create/', views.Inscription, name="Inscription_create"),

]