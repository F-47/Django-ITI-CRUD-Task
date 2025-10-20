from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from .forms import CourseForm, ManualCourseForm
import os

def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/courses_list.html', {'courses': courses})

def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('courses_list')
    else:
        form = CourseForm()
    return render(request, 'courses/course_form.html', {'form': form})

# CREATE (Manual Form)
def course_create_manual(request):
    if request.method == 'POST':
        form = ManualCourseForm(request.POST, request.FILES)
        if form.is_valid():
            Course.objects.create(
                code=form.cleaned_data['code'],
                name=form.cleaned_data['name'],
            )
            return redirect('courses_list')
    else:
        form = ManualCourseForm()
    return render(request, 'courses/course_form.html', {'form': form})

def course_update(request, code):
    course = get_object_or_404(Course, code=code)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('courses_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'courses/course_form.html', {'form': form})



def course_delete(request, code):
    course = get_object_or_404(Course, code=code)
    course.delete()
    return redirect('courses_list')

