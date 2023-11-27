from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.StudentList.as_view()),
    path('create-student/', views.StudentCreate.as_view()),
    path('student-retrieve/<int:pk>/', views.StudentRetrieve.as_view()),
    path('student-update/<int:pk>/', views.StudentUpdate.as_view()),
    path('student-delete/<int:pk>/', views.StudentDelete.as_view()),
]
