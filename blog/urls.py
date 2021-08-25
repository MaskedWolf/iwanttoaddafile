from django.urls import path
from . import views

urlpatterns = [
  path('', views.blog_index, name="blog_index"),
  path('createnew/', views.add_new_activity, name="create_new_activity")
]
