from django.contrib import admin
from .models import State, Activity, Category

# Register your models here.
admin.site.register(State)
admin.site.register(Category)
admin.site.register(Activity)
