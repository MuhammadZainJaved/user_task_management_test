from django.urls import path
from . import views
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_jwt.views import obtain_jwt_token

app_name = "user_auth"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("api-token-auth/", ObtainAuthToken.as_view()),
    path("api-jwt-auth/", obtain_jwt_token),
]
