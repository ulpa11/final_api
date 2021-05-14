from django.urls import path
from . import views

urlpatterns = [
    path("",views.apioverview,name="apioverview"),
    path("task-list/",views.tasklist,name="task-list"),
    path("task-create/",views.taskcreate,name="task-create"),
    path("index",views.index,name="index")
]