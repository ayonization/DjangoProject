from django.shortcuts import render
from .models import Profile
# Create your views here.


def profiles(request):
    #* Get all profiles from the db
    profiles = Profile.objects.all()
    context = {'profiles':profiles}
    return render(request,'users/profiles.html',context)

def userProfile(request,pk):
    #* Get user from primary key(id)
    profile = Profile.objects.get(id = pk)

    #* Skills with description 
    topSkills = profile.skill_set.exclude(description__exact = "")

    #* Skills without description
    otherSkills = profile.skill_set.filter(description = "")

    context = {'profile':profile,"topSkills" : topSkills,"otherSkills" : otherSkills}
    return render(request,'users/user-profile.html',context)