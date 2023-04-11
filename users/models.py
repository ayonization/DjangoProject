import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#* User model already built in to django so modifying it is risky
#* Profile model is like a replica of the user model with additional attributes
#* We define a one to one relationship of a profile with a user
class Profile(models.Model):
    
    #* User has one to one relationship with user model(built in to django) (one user one profile)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)

    name = models.CharField(max_length=200,blank=True,null=True)
    email = models.EmailField(max_length=500,blank=True,null=True)
    username = models.CharField(max_length=200,blank=True,null=True)
    location = models.CharField(max_length=200,blank=True,null=True)
    short_intro = models.CharField(max_length=200,blank=True,null=True)
    bio = models.TextField(blank=True,null=True)

    #* Uploaded images will be stored at static/images/profiles
    profile_image = models.ImageField(null=True,blank=True,upload_to='profiles/',default="profiles/user-default.png")

    social_github = models.CharField(max_length=200,blank=True,null=True)
    social_twitter = models.CharField(max_length=200,blank=True,null=True)
    social_linkedin = models.CharField(max_length=200,blank=True,null=True)
    social_youtube = models.CharField(max_length=200,blank=True,null=True)
    social_website = models.CharField(max_length=200,blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return str(self.user.username)
    
class Skill(models.Model) :

    #* Skill has a owner (linked using Profile)
    #* When a profile is deleted, its skills are also deleted
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)

    name = models.CharField(max_length=200,blank=True,null=True)
    description = models.TextField(null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return str(self.name)
