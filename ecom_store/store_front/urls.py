from . import views
from django.urls import path

# Urls for payments pages
# add comments when urls are set
urlpatterns = [
    path('', views.home, name='home'),
    path('view/<str:id>', views.single_view, name='single_view'),
    path('products', views.products, name='products'),
    path('search-results', views.search_results, name='search_results'),
    path('test', views.test, name='test')
]

