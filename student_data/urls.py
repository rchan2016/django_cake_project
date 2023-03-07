from django.urls import path
from . import views

urlpatterns = [
    path('student_info', views.student_info, name='student_info')
]
