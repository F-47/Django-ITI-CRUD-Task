from django import forms
from .models import Course
from django.forms import DateInput

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'name']
        
class ManualCourseForm(forms.Form):
    code = forms.CharField(max_length=10)
    name = forms.CharField(max_length=10)