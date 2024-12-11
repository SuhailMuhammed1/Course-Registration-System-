from django import forms
from .models import *

class CourseRegistrationForm(forms.Form):  # form for registering students
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    course = forms.ModelChoiceField(queryset=Course.objects.all(), empty_label="Select a course")

    def __init__(self, *args, **kwargs): # constructor
        available_courses = kwargs.pop('available_courses', None) # remove available_courses
        super().__init__(*args, **kwargs) # initialise super constructor
        if available_courses is not None: # check if available_courses 
            self.fields['course'].queryset = available_courses

class CourseForm(forms.ModelForm):
    class Meta: # generates form from model
        model = Course
        fields = ['title', 'description', 'maximum_capacity']
