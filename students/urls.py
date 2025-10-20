from django.urls import path
from . import views

urlpatterns = [
    path('', views.students_list, name='students_list'),
    path('create/', views.student_create, name='student_create'),
    path('create-manual/', views.student_create_manual, name='student_create_manual'),
    path('<int:pk>/edit/', views.student_update, name='student_update'),
    path('<int:pk>/delete/', views.student_delete, name='student_delete'),
]
