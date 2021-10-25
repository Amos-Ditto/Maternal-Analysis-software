from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
   path('', views.index, name='index'),
   path('home', views.homepage, name='home'),
   path('reports', views.forms, name='reports'),
   path('auth/login', LoginView.as_view(template_name='dapapp/login.html'),name='login'),
    path('auth/logout', LogoutView.as_view()),
   path('auth/signin', views.signin, name='signin')
]
