from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import User

def register(request):
  if request.method == "POST":
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      user = User.objects.get(username=form.cleaned_data["username"])
      user.first_name = form.cleaned_data["fname"]
      user.last_name = form.cleaned_data["lname"]
      user.save()
    return redirect("/")
  else:
    form = SignUpForm()

  return render(request, "register.html", {"form": form})

