from django.shortcuts import render,redirect

# Create your views here.

#* All views associated to projects app defined here

from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

# projectsList = [

#     {
#         'id':'1',
#         'title':'Ecommerce Website',
#         'description':'Better than Amazon'
#     },
#     {
#         'id':'2',
#         'title':'Portfolio Website',
#         'description':'Better than LinkedIn'
#     },
#     {
#         'id':'3',
#         'title':'Social Network',
#         'description':'Better than Facebook'
#     },
# ]

def projects(request):
    
    #* Passing data to templates using context dictionaries
    # page = 'projects'
    # number = 10
    # context = {'page':page,'number':number,'projects':projectsList}

    #* Query projects from database and store in a queryset
    projects = Project.objects.all()

    #* Store in a context to pass to the db
    context = {'projects':projects}
    return render(request,'projects/projects.html',context)

def project(request,pk):

    #* Creating object of project whose id passed in url and passing to template
    projectObj = None

    #* Get the project from the db where id = pk
    projectObj = Project.objects.get(id=pk)

    # for i in projectsList:
    #     if i['id'] == pk:
    #         projectObj = i

    return render(request,'projects/single-project.html',{'project':projectObj})

#* CRUD operations using model forms

#* Views for model forms

def createProject(request):

    #* Instantiate ProjectForm class
    form = ProjectForm()

    #* When model form is submitted, POST request is sent (form method is post)
    if request.method == 'POST':
        #print(request.POST)

        #* Create form object with data passed from modelform (via request)
        form = ProjectForm(request.POST)

        #* Check if form object is valid
        if form.is_valid():

            #* Save the data in database
            form.save()
            #* Redirect user to home page once saved
            return redirect('projects')

    context = {'form':form}
    return render(request,'projects/project_form.html',context)

#* Pass parameter to identify which project to update
def updateProject(request,pk):

    #* Instance of form for project to be updated
    project = Project.objects.get(id = pk)
    form = ProjectForm(instance=project)

    if request.method=='POST':

        #* Update form with data from post and save in db
        form = ProjectForm(request.POST,instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form':form}
 
    return render(request,'projects/project_form.html',context)

def deleteProject(request,pk):

    #* Object to be deleted
    project = Project.objects.get(id=pk)
    
    #* When button for deletion is clicked, a POST request is sent
    if request.method == 'POST':
        #* Delete the object
        project.delete()
        return redirect('projects')

    context = {'object' : project} 
    return render(request,'projects/delete_template.html',context)
