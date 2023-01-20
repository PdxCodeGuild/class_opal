from rest_framework import serializers
from students.models import Students

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ('first_name', 'last_name', 'cohort', 'fav_topic', 'fav_teacher')