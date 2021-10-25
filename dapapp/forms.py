from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import DeliveriesInfo, MaternalDeathsInfo

class SignUpForm(UserCreationForm):
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

	class Meta:
		model = User
		fields = ('username','email', 'password1', 'password2')


class delivariesForm(ModelForm):
	class Meta:
		model = DeliveriesInfo
		fields = ['subcountyname', 'facilityname', 'noofsuccessfulbirths',
		    'nooflivebirths', 'noofstillbirths']

class maternaldeathsForm(ModelForm):
	class Meta:
		model = MaternalDeathsInfo
		fields = '__all__'
