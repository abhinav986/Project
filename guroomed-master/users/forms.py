from django.contrib.auth.forms import UserCreationForm
from django import forms
# from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class RegistrationForm(UserCreationForm):
	first_name = forms.CharField(min_length=1, max_length=30, help_text='Please enter valid First Name.')
	last_name = forms.CharField(min_length=1, max_length=30, help_text='Please eneter valid Last Name')
	email = forms.EmailField(max_length=254, help_text='Please enter valid email address')
	password1 = forms.CharField(min_length=6, max_length=20, help_text='Please enter valid password')
	password2 = forms.CharField(min_length=6, max_length=20, help_text='Please enter valid password')

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.first_name = self.cleaned_data.get('first_name')
		user.last_name = self.cleaned_data.get('last_name')
		user.email = self.cleaned_data.get('email')
		user.username = self.cleaned_data.get('email')
		user.password1 = self.cleaned_data.get('password1')
		user.password2 = self.cleaned_data.get('password2')

		if commit:
			user.save()

		return user


class EditForm(ModelForm):
	first_name = forms.CharField(min_length=1, max_length=30, help_text='Please enter valid First Name.')
	last_name = forms.CharField(min_length=1, max_length=30, help_text='Please eneter valid Last Name')
	email = forms.EmailField(max_length=254, help_text='Please enter valid email address')

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

	def save(self, commit=True):
		user = super(EditForm, self).save(commit=False)
		user.first_name = self.cleaned_data.get('first_name')
		user.last_name = self.cleaned_data.get('last_name')
		user.email = self.cleaned_data.get('email')
		user.username = self.cleaned_data.get('email')

		if commit:
			user.save()

		return user