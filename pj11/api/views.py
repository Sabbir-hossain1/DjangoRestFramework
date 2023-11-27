from django.shortcuts import render
from rest_framework.decorators import api_view
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.response import Response
# Create your views here.

@api_view(['GET','POST','PUT','PATCH', 'DELETE'])
def student_api(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data inserted Successfully"})
        return Response(serializer.errors)
    
    if request.method == 'PUT':
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": 'full Updated data successfully'})
        return Response(serializer.errors)
    
    if request.method == 'PATCH':
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            raise Response({"msg": 'partial Updated data successfully'})
        return Response(serializer.errors)
    
    if request.method == 'DELETE':
        id = pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg': 'data deleted successfully'})