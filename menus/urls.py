from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls import url

from menus.views import (
    ItemListView,
    ItemCreateView,
    ItemUpdateView,
)

urlpatterns = [

    url(r'^$', ItemListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', ItemUpdateView.as_view(), name='detail'),
    path('create/', ItemCreateView.as_view(), name='create'),
    
]