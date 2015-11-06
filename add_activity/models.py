from django.db import models
from django import forms

class formInfo(models.Model):
	vote_count = models.CharField(max_length = 100000,blank = True, null = True)
	ask_activity = forms.CharField(label='Enter a new activity', max_length=30)
	ask_top_attribute = forms.CharField(label='Enter a attributes',max_length=30)
	ask_team = [('team','Team Activity'),
		 ('single','Not  Team Activity')]
	answer_team = forms.ChoiceField(choices=ask_team, widget=forms.RadioSelect())
	ask_intensity = [('intense','Intense Activity'),
		 ('notIntense','Not Intense Activity')]
	answer_intenseity = forms.ChoiceField(choices=ask_intensity, widget=forms.RadioSelect())
	def __unicode__(self):
		return self.name
