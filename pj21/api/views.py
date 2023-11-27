from api.models import Student
from api.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [DjangoModelPermissions]
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    