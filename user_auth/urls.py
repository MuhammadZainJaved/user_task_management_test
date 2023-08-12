from django.urls import path
from . import views

app_name = "user_auth"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("api-token-auth/", views.CustomAuthToken.as_view()),
]
