from django.shortcuts import render
from rest_framework.decorators import api_view
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.response import Response
# Create your views here.

@api_view(['GET','POST','PUT', 'DELETE'])
def student_api(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = StudentSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data inserted Successfully"})
        return Response(serializer.errors)
    
    if request.method == 'PUT':
        id = request.data.get('id') 
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            raise Response({"msg": 'Updated data successfully'})
        return Response(serializer.errors)
    
    if request.method == 'DELETE':
        id = request.data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg': 'data deleted successfully'})