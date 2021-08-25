from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from blog.models import Activity
from .forms import ActivityForm

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
    form = ActivityForm(request.POST) 
    # request.FILES)
    if form.is_valid():
      # image=form.cleaned_data["image"]
      obj = Activity(
        username=request.user,
        shopname=form.cleaned_data["shopname"],
        descriptions=form.cleaned_data["descriptions"],
        category=form.cleaned_data["category"],
        state=form.cleaned_data["state"],
        # image=image,
      )
      obj.save()

  context = {
    "form": form,
  }
  return render(request, "new_activity.html", context)