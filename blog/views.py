from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
from blog.models import Activity, State
from .forms import ActivityForm
from django.contrib import messages
from sop.forms import Landing_form


def blog_index(request):
    """Display all activities """
    posts = Activity.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)


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
  }
  return render(request, "new_activity.html", context)

def portal(request):
  return render(request, "portal.html", {})
"""
def portal(request):
  form = Landing_form()
  return render(request, "test.html", {"form": form})
"""

# obj = State.set(
# 	username=request.user,
# 	shopname=form.cleaned_data["shopname"],
# 	descriptions=form.cleaned_data["descriptions"],
# 	state=form.cleaned_data["state"],
# 	category=form.cleaned_data["category"],
# 	img = img,
# )
# obj.save()
			


