from django.db import models
import uuid
from users.models import Profile
# Create your models here.
#* Define tables in database

class Project(models.Model):

    #* Many to one relationship 
    owner = models.ForeignKey(Profile,null=True,blank=True,on_delete=models.SET_NULL)

    title = models.CharField(max_length=200)
    
    #* Blank entries allowed in db (null=true)
    #* Blank post requests (form submits) allowed (blank=true)
    description = models.TextField(null=True,blank=True)

    #* User uploaded image
    featured_image = models.ImageField(null=True,blank=True,default='default.jpg')
    
    demo_link = models.CharField(max_length=2000,null=True,blank=True)
    source_link = models.CharField(max_length=2000,null=True,blank=True)
    
    #* Automatically add timestamp for when record created
    created_at = models.DateTimeField(auto_now_add=True)
    
    #* Many to many relationship
    #* One project has multiple tags (react, node, django)
    #* One tag can can have multiple projects (react in 3 projects, django in 2)
    tags = models.ManyToManyField('Tag',blank=True)
    
    vote_total = models.IntegerField(default=0,null=True,blank=True)
    vote_ratio = models.IntegerField(default=0,null=True,blank=True)

    #* Setting uuid as primary key, not editable
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)  
    
    #* Model instances represented as string values instead of object names
    def __str__(self) :
        return self.title


class Review(models.Model):

    #* Create tuple with two choices for user to choose from 
    VOTE_TYPE = (
        ('up','Up Vote'),
        ('down','Down Vote')
    )
    
    #* One to Many Relationship
    #* Foreign key, which project is this review for?
    #* If project is deleted, delete (cascade) all associated reviews too
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    
    body = models.TextField(null=True,blank=True)
    value = models.CharField(max_length=200,choices=VOTE_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    def __str__(self) :
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    def __str__(self) :
        return self.name
