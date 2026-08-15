from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("cadastro/", views.cadastro, name="cadastro"),
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),
]
