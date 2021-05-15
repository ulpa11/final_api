from django.urls import path
from . import views

urlpatterns = [

    path("", views.index, name="index"),
    path("apioverview",views.apioverview,name="apioverview"),
    path("task-list/",views.tasklist,name="task-list"),
    path("task-create/",views.taskcreate,name="task-create"),

]