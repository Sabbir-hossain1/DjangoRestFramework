from rest_framework import serializers
from api.models import Student

#Validators functions 
def start_with_s(value):
    if value[0] != 's':
        raise serializers.ValidationError('Name should be start with S')

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100,validators=[start_with_s])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
    
    #field level Validation
    def validate_roll(self,value):
        if value>=200:
            raise serializers.ValidationError('Seat Full')
        return value
    
    #object level validation (multiple field validation)

    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')

        if nm.lower() == 'ratul' and  ct.lower() != 'chandpur':
            raise serializers.ValidationError('City must be Chandpur for Sabbir')
        return data
        