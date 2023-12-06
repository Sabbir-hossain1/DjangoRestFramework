from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/',views.LCStudent.as_view()),
    path('students/<int:pk>/', views.RUDStudent.as_view()),
]
