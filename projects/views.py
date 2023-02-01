from django.shortcuts import render

# Create your views here.

#* All views associated to projects app defined here

from django.http import HttpResponse

projectsList = [

    {
        'id':'1',
        'title':'Ecommerce Website',
        'description':'Better than Amazon'
    },
    {
        'id':'2',
        'title':'Portfolio Website',
        'description':'Better than LinkedIn'
    },
    {
        'id':'3',
        'title':'Social Network',
        'description':'Better than Facebook'
    },
]

def projects(request):
    
    #* Passing data to templates using context dictionaries
    page = 'projects'
    number = 10
    context = {'page':page,'number':number,'projects':projectsList}
    return render(request,'projects/projects.html',context)

def project(request,pk):

    #* Creating object of project whose id passed in url and passing to template
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request,'projects/single-project.html',{'project':projectObj})
