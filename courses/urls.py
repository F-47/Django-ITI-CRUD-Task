from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses_list, name='courses_list'),
    path('create/', views.course_create, name='course_create'),
    path('create-manual/', views.course_create_manual, name='course_create_manual'),
    path('<str:code>/edit/', views.course_update, name='course_update'),
    path('<str:code>/delete/', views.course_delete, name='course_delete'),
]
