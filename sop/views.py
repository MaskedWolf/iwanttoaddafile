from django.shortcuts import render
from .forms import Landing_form 
from .models import Sopdetail

# Create your views here.
def landing(request):
	test = Sopdetail.objects.all()
	form = Landing_form()

	if request.method == 'POST':
		form = Landing_form(request.POST)
		if form.is_valid():
			state = form.cleaned_data["state"]
			vaccination_state = form.cleaned_data["fully_vaccinated"]
		
			return render(request, "landing.html", {"state":state,"vaccinated":vaccination_state,"test": test,"form": form,})
        
	context = {
		"test": test,
		"form": form,
	}
	return render(request, "landing.html", context)

#def result(request):




	#context = {
		
#	}
#	return render(request, "result.html", context)