from django.db import models

# Create your models here.

class Sop_detail(models.Model):

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
	state = models.CharField(max_length=50,choices=states,null=True)

	ph = (
		(1, 1),
		(2, 2),
		(3, 3),
	)
	phase = models.IntegerField(choices=ph,null=True)


	Description_dining_vaccinated = models.CharField(max_length=200,null=True)
	Description_dining_unvaccinated = models.CharField(max_length=200,null=True)
	Description_travel = models.CharField(max_length=200,null=True)
	Description_transport = models.CharField(max_length=200,null=True)
	Description_religion = models.CharField(max_length=200,null=True)
	Description_market = models.CharField(max_length=200,null=True)
	Description_shopping = models.CharField(max_length=200,null=True)

	def __str__(self):
		return self.state

	crtDate = models.DateTimeField(auto_now_add=True) 