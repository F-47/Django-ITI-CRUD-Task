from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm, ManualStudentForm
import os

def students_list(request):
    students = Student.objects.all()
    return render(request, 'students/students_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('students_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

# CREATE (Manual Form)
def student_create_manual(request):
    if request.method == 'POST':
        form = ManualStudentForm(request.POST, request.FILES)
        if form.is_valid():
            Student.objects.create(
                name=form.cleaned_data['name'],
                age=form.cleaned_data['age'],
                dob=form.cleaned_data['dob'],
                image=form.cleaned_data.get('image')
            )
            return redirect('students_list')
    else:
        form = ManualStudentForm()
    return render(request, 'students/student_form.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form})



def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if student.image:
        image_path = student.image.path
        if os.path.isfile(image_path):
            os.remove(image_path)
    student.delete()
    return redirect('students_list')

