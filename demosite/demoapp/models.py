# File: models.py
# Group: 12 (Team Intrinsic)
# Members: Kevin Mann, Derek Fong, Allison Ng
# CMPT470: Technical Evaluation
#
# Date of Creation: Feb 22, 2012
# Revised: Feb 24, 2012
#
# Description: Defines the models for the demoapp which includes:
#			   - Poll
#			   - Choice
#			   - Voted

from django.db import models
from django.contrib.auth.models import User

# Defines the Poll model that will consist of:
# - question - the question of the created poll (max of 200 characters)
# - pub_date - the date the poll was published
class Poll(models.Model):
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __unicode__(self):
		return self.question

# Defines the Choice model that will consist of:
# - poll - the poll associated with the choice
# - choice - the choice for a particular question (max of 200 characters)
# - votes - the number of votes for the choice
class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice = models.CharField(max_length=200)
	votes = models.IntegerField()
	def __unicode__(self):
		return self.choice

# Defines the Voted model that will consist of:
# - pollNumber - an associated poll id that has been voted for
# - userNumber - an associated user that has voted
# - vote_time - the date which the vote was casted by the user
class Voted(models.Model):
	pollNumber = models.IntegerField()
	userNumber = models.IntegerField()
	vote_time = models.DateTimeField('date voted')
	def __unicode__(self):
		return u'%s' %self.userNumber
