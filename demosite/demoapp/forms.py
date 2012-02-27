# File: forms.py
# Group: 12 (Team Intrinsic)
# Members: Kevin Mann, Derek Fong, Allison Ng
# CMPT470: Technical Evaluation
#
# Date of Creation: Feb 23, 2012
# Revised: Feb 23, 2012
#
# Description: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
	email = forms.EmailField(label="E-Mail")
	first_name = forms.CharField(label='First Name')
	last_name = forms.CharField(label='Last Name')	

	class Meta:
		model = User
		fields = ("username", "email", "first_name", "last_name",  )

	def clean_email(self):
		email = self.cleaned_data["email"]
	
		try:
			User.objects.get(email=email)
		except User.DoesNotExist:
			return email

		raise forms.ValidationError("A user with that email address already exists.")

