from django.urls import path
from . import views
#* Activate venv -> source bin/activate

#* All urls associated to projects app defined here

urlpatterns = [

    #* Root domain (home page)
    path('',views.projects,name = "projects"),
    #* Parametrized url 
    path('project/<str:pk>/',views.project,name='project'),

    path('create-project/',views.createProject,name="create-project"),
    path('update-project/<str:pk>/',views.updateProject,name='update-project'),
    path('delete-project/<str:pk>/',views.deleteProject,name='delete-project'),
]