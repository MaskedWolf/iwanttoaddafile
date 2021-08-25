from django.db import models

# Create your models here.

class Sopdetail(models.Model):
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
		(3, 3)
	)

	phase = models.IntegerField(choices=ph,null=True)

	vaccine = models.BooleanField(default=False)
	#i quit fk this shit this is bullshit never in my life i have ever seen such a bullshit solution like wtf this is just gay im done with life and there is no god wtf is code 

	Description_Arts = models.CharField(max_length=200,null=True)

	Description_Receation = models.CharField(max_length=200,null=True)

	Description_Health = models.CharField(max_length=200,null=True)

	Description_House_Visiting = models.CharField(max_length=200,null=True)

	Description_Market = models.CharField(max_length=200,null=True)

	Description_Meeting = models.CharField(max_length=200,null=True)

	Description_School = models.CharField(max_length=200,null=True)

	Description_Shop = models.CharField(max_length=200,null=True)

	Description_Sports = models.CharField(max_length=200,null=True)

	Description_Taxi = models.CharField(max_length=200,null=True)

	Description_Dine_in = models.CharField(max_length=200,null=True)

	Description_Religious = models.CharField(max_length=200,null=True)

	Description_gathering = models.CharField(max_length=200,null=True)

	Description_Travel = models.CharField(max_length=200,null=True)

	Description_others_y = models.CharField(max_length=200,null=True)

	Description_others_n = models.CharField(max_length=200,null=True)

	def __str__(self):
		return self.state

	crtDate = models.DateTimeField(auto_now_add=True)
