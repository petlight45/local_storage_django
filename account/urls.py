from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'user'

urlpatterns = [
  path('signin', views.signin, name='signin'),
  path('signup', views.signup, name='signup'),
  path('logout', auth_views.LogoutView.as_view(), name='logout'),
]