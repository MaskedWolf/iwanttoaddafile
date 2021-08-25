from django.shortcuts import render
from .forms import Landing_form 


# Create your views here.
def landing(request):

	form = Landing()
	if request.method == 'POST':
		form = Landing(request.POST)
		if form.is_valid():
			pass
          
          
          



	context = {
		"form":form,

	}
	return render(request, "landing.html", context)

def result(request):




	context = {
		
	}
	return render(request, "result.html", context)