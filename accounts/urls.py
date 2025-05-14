from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "accounts"
urlpatterns = [
 path('signup/', views.signup_choice, name='signup_choice'),
 path('signup/regular/', views.regular_user_signup_view, name='regular_user_signup'),
 path('signup/organization/', views.organization_signup_view, name='organization_signup'),
 #path('login/', views.login_view, name='login'),
 path('logout/', views.logout_view, name='logout'),
 path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
]