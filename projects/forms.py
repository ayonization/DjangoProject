
#* Define model forms here
#* Django automatically builds forms based on pre defined models

from django.forms import ModelForm
from .models import Project

from django import forms


#* Model form defined as class
class ProjectForm(ModelForm):
    class Meta:

        #* Model for which modelform is made
        model = Project
        #* Fields from model to be included in form
        fields = ['title','featured_image','description','demo_link','source_link','tags']

        #* Tags now displayed as checkboxes
        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
        }

    def __init__(self,*args,**kwargs) :
        super(ProjectForm,self).__init__(*args,**kwargs)

            # self.fields['title'].widget.attrs.update(
            #     {'class':'input','placeholder':'Add Title'})

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
            