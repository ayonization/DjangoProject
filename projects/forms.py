
#* Define model forms here
#* Django automatically builds forms based on pre defined models

from django.forms import ModelForm
from .models import Project

#* Model form defined as class
class ProjectForm(ModelForm):
    class Meta:

        #* Model for which modelform is made
        model = Project
        #* Fields from model to be included in form
        fields = ['title','featured_image','description','demo_link','source_link','tags']