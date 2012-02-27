# File: forms.py
# Group: 12 (Team Intrinsic)
# Members: Kevin Mann, Derek Fong, Allison Ng
# CMPT470: Technical Evaluation
#
# Date of Creation: Feb 23, 2012
# Revised: Feb 23, 2012
#
# Description: Extends the UserCreationForm model

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

# Extends the UserCreationModel to add email, first_name, last_name fields.
# - Creates CharFields for each field.

class RegisterForm(UserCreationForm):
	email = forms.EmailField(label="E-Mail")
	first_name = forms.CharField(label='First Name')
	last_name = forms.CharField(label='Last Name')	
	
	#Extends the User model with the username, email, first_name, last_name fields.
	class Meta:
		model = User
		fields = ("username", "email", "first_name", "last_name",  )

		# "Cleans" the email field to ensure it's valid.
		# - Ensures that the email address doesn't already exist in the database
		# - If it already exists, output validation error
	def clean_email(self):
		email = self.cleaned_data["email"]
	
		try:
			User.objects.get(email=email)
		except User.DoesNotExist:
			return email

		raise forms.ValidationError("A user with that email address already exists.")

