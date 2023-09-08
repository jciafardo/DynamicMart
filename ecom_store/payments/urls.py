from . import views
from django.urls import path

# Urls for payments pages
urlpatterns = [

    path('checkout-success', views.checkout_success, name='checkout_success'),
    path('payments-cancel', views.checkout_cancel, name='payments-cancel'),

]




