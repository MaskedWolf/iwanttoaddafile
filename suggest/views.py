from django.shortcuts import render
import random
from .models import suggestion

def suggest(request):
  fetch_all = suggestion.objects.all()
  fetch = suggestion.objects.get(place=1)
  if request.method == "GET":
    length = 0
    for i in fetch_all:
      length += 1
    print(length)
    num = random.randint(1, length)
    print(num)
    fetch = suggestion.objects.get(place=num)
    print(fetch.name)
    return render(request, "random.html", {"suggest": fetch})
  else:
    fetch = suggestion.objects.get(place=1)
  
  return render(request, "random.html", {"suggest": fetch})

# Create your views here.
