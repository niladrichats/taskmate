from django.contrib import admin
# from todolist_app.models import TaskList
from .models import TaskList

# Register your models here.
admin.site.register(TaskList)
