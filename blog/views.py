from django.shortcuts import render
from itertools import chain
# from django.http import HttpResponse

# from django.contrib.auth.decorators import login_required

# Create your views here.
from blog.models import Activity, State
from .forms import ActivityForm, search
from django.contrib import messages
from sop.forms import Landing_form


def blog_index(request):
  if request.method == "POST":
    form = search(request.POST)
    searched = request.POST["keyword"]
    fetch1 = Activity.objects.filter(shopname__contains=searched).order_by('-created_on')
    fetch2 = Activity.objects.filter(username__contains=searched).order_by('-created_on')
    fetch3 = Activity.objects.filter(descriptions__contains=searched).order_by('-created_on')
    fetch4 = {}
    for i in Activity.objects.all():
      for j in i.category.all():
        if j == searched:
          fetch5 = list(j)
          fetch4 = list(chain(fetch4, fetch5))
    fetch = list(chain(fetch1, fetch2, fetch3, fetch4))
    context = {
      "form": form,
      "posts": fetch,
    }
  else:
    form = search()
    posts = Activity.objects.all().order_by('-created_on')
    context = {
        "form": form,
        "posts": posts,
    }
  return render(request, "blog_index.html", context)

"""
    Display all activities
    posts = Activity.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)
"""

# @login_required(login_url='login/')
def add_new_activity(request):
  form = ActivityForm()
  if request.method == 'POST':
    # print(request.POST)
    form = ActivityForm(request.POST,request.FILES)
    if form.is_valid():
      state=form.cleaned_data["state"]
      img = form.cleaned_data["image"]
      username=request.user
      shopname=form.cleaned_data["shopname"]
      descriptions=form.cleaned_data["descriptions"]
      category=form.cleaned_data["category"]
      instance = Activity.objects.create(
        username=username,
        shopname=shopname,
        descriptions=descriptions,
        # category=category,
        image=img,
      )
      instance.state.set(state)
      instance.category.set(category)

      messages.success(request, 'Form submission successful')

  context = {
    "form": form,
    "user": request.user,
  }
  return render(request, "new_activity.html", context)

def portal(request):
  return render(request, "portal.html", {})

# def portal(request):
#   form = Landing_form()
#   return render(request, "test.html", {"form": form})


# obj = State.set(
# 	username=request.user,
# 	shopname=form.cleaned_data["shopname"],
# 	descriptions=form.cleaned_data["descriptions"],
# 	state=form.cleaned_data["state"],
# 	category=form.cleaned_data["category"],
# 	img = img,
# )
# obj.save()
			


