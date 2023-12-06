from django.shortcuts import render
from rest_framework.response import Response
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets

class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        print("-----------list------------")
        print('basename: ', self.basename)
        print('Action: ', self.action)
        print('Detail:', self.detail)
        print('suffix:', self.suffix)
        print('name:', self.name)
        print("Description: ", self.description)

        stud = Student.objects.all()
        serializer = StudentSerializer(stud, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        print("-----------Retrieve------------")
        print('basename: ', self.basename)
        print('Action: ', self.action)
        print('Detail:', self.detail)
        print('suffix:', self.suffix)
        print('name:', self.name)
        print("Description: ", self.description)
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
    
    def create(self, request):
        print("-----------Create------------")
        print('basename: ', self.basename)
        print('Action: ', self.action)
        print('Detail:', self.detail)
        print('suffix:', self.suffix)
        print('name:', self.name)
        print("Description: ", self.description)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data inserted'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):
        print("-----------update------------")
        print('basename: ', self.basename)
        print('Action: ', self.action)
        print('Detail:', self.detail)
        print('suffix:', self.suffix)
        print('name:', self.name)
        print("Description: ", self.description)

        id = pk
        stud = Student.objects.get(id=id)
        serializer = StudentSerializer(stud, data=request.data)
        if serializer.is_valid():
            return Response({"msg": 'Complete data updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def partial_update(self,request,pk):
        print("-----------partial update------------")
        print('basename: ', self.basename)
        print('Action: ', self.action)
        print('Detail:', self.detail)
        print('suffix:', self.suffix)
        print('name:', self.name)
        print("Description: ", self.description)
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response({"msg": 'Partial data Updated Successfully'})
    
    def destroy(self, request, pk):
        print("-----------destroy------------")
        print('basename: ', self.basename)
        print('Action: ', self.action)
        print('Detail:', self.detail)
        print('suffix:', self.suffix)
        print('name:', self.name)
        print("Description: ", self.description)
        id = pk
        stud = Student.objects.get(id=id)
        stud.delete()
        return Response({"msg": 'Data deleted successfully'})