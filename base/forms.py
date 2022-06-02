

from django import forms 
from .models import Course, Application

class CourseApplicationForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'schools']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'course', 'grade']