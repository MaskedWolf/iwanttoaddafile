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
    form = ActivityForm(request.POST)
    # if form.is_valid():
    #   form = Activity(
    #     # edit this
    #     author=form.cleaned_data["author"],
    #     body=form.cleaned_data["body"],
    #   )
    #   form.save()

  context = {
      "form": form,
  }
  return render(request, "new_activity.html", context)