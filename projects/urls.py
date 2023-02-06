from django.urls import path
from . import views
#* Activate venv -> source bin/activate

#* All urls associated to projects app defined here

urlpatterns = [

    #* Root domain (home page)
    path('',views.projects,name = "projects"),
    #* Parametrized url 
    path('project/<str:pk>/',views.project,name='project'),
]