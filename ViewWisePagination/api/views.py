from django.shortcuts import render
from rest_framework.generics import ListAPIView
from api.models import Student
from api.serializers import StudentSerializer
from api.myPagination import MyPagination

# Create your views here.
class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyPagination