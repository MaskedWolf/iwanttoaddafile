from django.shortcuts import render
from .forms import Landing_form 
from .models import Sopdetail

# Create your views here.
""""
def landing(request):
	test = Sopdetail.objects.all()
	form = Landing_form()

  if request.method == "POST":
    form = request.POST
    print(form)


	if request.method == 'POST':
		form = Landing_form(request.POST)
    print(form)
		if form.is_valid():
      state = form.cleaned_data["state"] 
       
	context = {
		"test": test,
		"form": form,
		
	}
	return render(request, "landing.html", context)

#def result(request):




	#context = {
		
#	}
#	return render(request, "result.html", context)
"""
def landing(request):
  state = None
  vaccine = None
  obj = None
  obj1 = None

  if request.method == 'POST':
      form = Landing_form(request.POST)
      if form.is_valid():
        obj = Sopdetail.objects.get(state=form.cleaned_data["state"])
        state = form.cleaned_data["state"]
        vaccine = form.cleaned_data["fully_vaccinated"]
        insert = {
          "form": Landing_form(request.POST),
          "test": obj,
					"vaccine": vaccine,
        }
        return render(request, "result.html", insert)
         
  else:
    form = Landing_form()

  return render(request, "landing.html", {"form":form})