from . import views
from django.urls import path

# Urls for payments pages
urlpatterns = [

    path('upload-products', views.upload_products, name='upload-products'),

]

