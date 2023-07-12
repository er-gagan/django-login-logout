
from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.handleLoginForm),
    path('login', views.handleLogin),
    path('welcome', views.handleWelcome),
    path('logout', views.handleLogout),
    path('public', TemplateView.as_view(template_name='public.html'))
]
