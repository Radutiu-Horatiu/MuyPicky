from django import forms
from restaurant.models import RestaurantLocation
from .models import Item

class ItemForm(forms.ModelForm):

	class Meta:
		model = Item
		fields = [

			'restaurant',
			'name',
			'contents',
			'excludes',
			'public'

		]
	
	def __init__(self, user=None, *args, **kwargs):
		super(ItemForm, self).__init__(*args, **kwargs)
		self.fields['restaurant'].queryset = RestaurantLocation.objects.filter(owner=user)#.exclude(item__isnull=False)