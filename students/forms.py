from django import forms
from .models import Student
from django.forms import DateInput

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'image', 'dob', 'courses']
        widgets = {
            'dob': DateInput(attrs={'type': 'date'}),
        }

class ManualStudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField(min_value=1)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    image = forms.ImageField(required=False)
