from django import forms
from .models import *

class CourseRegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    course = forms.ModelChoiceField(queryset=Course.objects.all(), empty_label="Select a course")

    def __init__(self, *args, **kwargs):
        available_courses = kwargs.pop('available_courses', None)
        super().__init__(*args, **kwargs)
        if available_courses is not None:
            self.fields['course'].queryset = available_courses

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'maximum_capacity']