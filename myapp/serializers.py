from rest_framework import serializers
from .models import SchoolModel, StandardModel, StudentModel


class StandardModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = StandardModel
        fields = ('number', 'teacher', 'school')


class StudentModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentModel
        fields = ('name', 'age', 'standard')


class SchoolModelSerializer(serializers.ModelSerializer):
    standard = StandardModelSerializer(many=True)
    student = StudentModelSerializer(many=True)

    class Meta:
        model = SchoolModel
        fields = (
            'name',
            'head_master',
            'standard',
            'student',
        )

    def create(self, validated_data):
        standard = validated_data.pop('standard')
        print(standard)
        students = validated_data.pop('student')
        print(students)
        school = SchoolModel.objects.create(**validated_data)
        print(school)
        standard = StandardModel.objects.create(**standard, school=school)
        for st in students:
            StudentModel.objects.create(**st, standard=standard)
        return school

