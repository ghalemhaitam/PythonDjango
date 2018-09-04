# New Method
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name="login"),
    path('inscription/', views.InscriptionView.as_view(), name="Inscription"),
    
    #path('inscription/create/', views.Inscription, name="Inscription_create"),

]