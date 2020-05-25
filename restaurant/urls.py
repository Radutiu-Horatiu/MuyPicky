from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls import url

from restaurant.views import (
	RestaurantListView,
	RestaurantCreateView,
    RestaurantUpdateView,
)

urlpatterns = [

    url(r'^$', RestaurantListView.as_view(), name='restaurants'),
    path('create/', RestaurantCreateView.as_view(), name='add-restaurant'),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantUpdateView.as_view(), name='restaurant-detail'),
    
]