from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, UpdateView, ListView, CreateView

from .forms import RestaurantLocationCreateForm
from .models import RestaurantLocation

class RestaurantListView(LoginRequiredMixin, ListView):
	template_name = 'restaurants/restaurants_list.html'
	login_url = '/restaurant/login/'
	success_url = '/restaurant/restaurants/'

	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user)

class RestaurantCreateView(LoginRequiredMixin, CreateView):
	form_class = RestaurantLocationCreateForm
	template_name = 'form.html'
	login_url = '/restaurant/login/'
	success_url = '/restaurant/restaurants/'

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.owner = self.request.user

		return super(RestaurantCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Add Restaurant'
		return context

class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
	form_class = RestaurantLocationCreateForm
	template_name = 'restaurants/detail-update.html'
	login_url = '/restaurant/login/'
	#success_url = '/restaurant/restaurants/'

	def get_context_data(self, *args, **kwargs):
		context = super(RestaurantUpdateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Update'
		return context

	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user)