# Store your serializers here.
# Serializer is a place to make transformations
# At least one serializer per model

from rest_framework import serializers
from students.models import Student

# serializers.ModelSerializer class provided by Django provides
# a useful shortcut for creating serializers that deal with model instances + querysets
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # Don't have to include all information (such as omitting id) but in this case want everything the Student class has
        # represented as strings
        fields = (
            'first_name',
            'last_name',
            'cohort',
            'favorite_topic',
            'teacher',
            'capstone',
            'id'
            )
