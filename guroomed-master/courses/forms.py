from django.forms import ModelForm
from .models import Course
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


# Create the form class.
class CourseForm(ModelForm):
	class Meta:
		model = Course
		fields = ['course_subcategory_id', 'course_language_id', 'instructor_id', 'title', 'subtitle', 'ratings', 'rating_count', 'students_enrolled', 'what_will_i_learn', 'requirements', 'description', 'preview_video_url', 'preview_image_url', 'price', 'discount', 'no_lectures', 'no_hours', 'level', 'slug', 'tags']


class SignupForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

	def save(self, commit=True):
		user = super(SignupForm, self).save(commit=False)
		user.first_name = self.cleaned_data.get('first_name')
		user.last_name = self.cleaned_data.get('last_name')
		user.email = self.cleaned_data.get('email')
		user.username = self.cleaned_data.get('email')

		if commit:
			user.save()
		return user