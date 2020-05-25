from .views import ProfileDetailView, ProfileFollowToggle 
from django.conf.urls import url
from django.urls import path

urlpatterns = [
	
	path('profile-follow/', ProfileFollowToggle.as_view(), name='follow'),
	url(r'^(?P<username>[\w-]+)/$', ProfileDetailView.as_view(), name='detail'),
]