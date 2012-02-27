# File: admin.py
# Group: 12 (Team Intrinsic)
# Members: Kevin Mann, Derek Fong, Allison Ng
# CMPT470: Technical Evaluation
#
# Date of Creation: Feb 22, 2012
# Revised: Feb 24, 2012
#
# Description: Extension of the admin interface model

from demoapp.models import Poll
from demoapp.models import Choice
from django.contrib import admin

# Customizes the Choice model:
# - Displayed tabular in-line
# - Sets the default display of empty choices to 3
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

# Customizes the Poll model:
# - Sets the fields and associated display names
# - Displays in-line
# - Sets the display of polls to show the question and when it was made
class PollAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 			{'fields': ['question']}),
		('Date Information', 	{'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question', 'pub_date') 

# Enables the Poll app to be managed on the admin interface
admin.site.register(Poll, PollAdmin)
