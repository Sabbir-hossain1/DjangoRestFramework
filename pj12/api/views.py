from django.shortcuts import render
from rest_framework.views import APIView
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class StudentAPI(APIView):
    def get(self,request, pk=None, format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data inserted Successfully"})
        return Response(serializer.errors)
    
    def put(self, request,pk, format=None):
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": 'full Updated data successfully'})
        return Response(serializer.errors)
    
    def patch(self, request,pk, format=None):
        print("patch request received")
        id = pk
        print("id:",id)
        stu = Student.objects.get(id=id)
        print("student: ",stu)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": 'partial Updated data successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors)
    
    def delete(self, requst, pk, format=None):
        id = pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg': 'data deleted successfully'})