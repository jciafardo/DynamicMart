from . import views
from django.urls import path

# Urls for accounts pages
urlpatterns = [
    path('login', views.login_user, name='login'),
    path('register', views.register, name='register'),
    path('accounts', views.accounts, name='accounts'),
    path('logout', views.logout_user, name='logout')

]