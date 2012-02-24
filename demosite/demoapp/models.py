from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Poll(models.Model):
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __unicode__(self):
		return self.question

class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice = models.CharField(max_length=200)
	votes = models.IntegerField()
	def __unicode__(self):
		return self.choice

class Voted(models.Model):
	pollNumber = models.IntegerField()
	userNumber = models.IntegerField()
	vote_time = models.DateTimeField('date voted')
	def __unicode__(self):
		return u'%s' %self.userNumber
