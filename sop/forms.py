from django import forms

class Landing_form(forms.Form):

	states = (
		('JOHOR', 'Johor'),
		('KEDAH', 'Kedah'),
		('KELANTAN', 'Kelantan'),
		('MALACCA', 'Malacca'),
		('NEGERI SEMBILAN','Negeri Sembilan'),
		('PAHANG', 'Pahang'),
		('PENANG', 'Penang'),
		('PERAK', 'Perak'),
		('PERLIS', 'Perlis'),
		('SABAH', 'Sabah'),
		('SARAWAK', 'Sarawak'),
		('SELANGOR', 'Selangor'),
		('TERENGGANU', 'Terengganu'),
		('KUALA LUMPUR', 'Kuala Lumpur'),
		('LABUAN', 'Labuan'),
		('PUTRAJAYA', 'Putrajaya'),
	)
	state = forms.ChoiceField(choices=states)
	fully_vaccinated = forms.BooleanField(required = False)