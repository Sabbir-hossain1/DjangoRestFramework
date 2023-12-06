
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', views.StudentListCreate.as_view()),
    path('students/<int:pk>/', views.StudentRetrieveUpdateDelete.as_view()),
]
