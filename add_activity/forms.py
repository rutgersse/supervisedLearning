from django import forms

class askAct(forms.Form):
	ask_activity = forms.CharField(label='Enter a new activity', max_length=30)

class askAtt(forms.Form):
	ask_top_attribute = forms.CharField(label='Enter a attributes',max_length=30)

class askTeam(forms.Form):
    ask_team = [('team','Team Activity'),
		 ('single','Not  Team Activity')]
    answer_team = forms.ChoiceField(choices=ask_team, widget=forms.RadioSelect())

class askInte(forms.Form):
	ask_intensity = [('intense','Intense Activity'),
		 ('notIntense','Not Intense Activity')]
	answer_intenseity = forms.ChoiceField(choices=ask_intensity, widget=forms.RadioSelect())
