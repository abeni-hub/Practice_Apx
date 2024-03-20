from rest_framework import serializers
from .models import Course, Module ,Scholarship

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['module_id', 'module_name']

class CourseSerializer(serializers.ModelSerializer):
    # module = ModuleSerializer()

    class Meta:
        model = Course
        fields = ['id', 'featured_img', 'course_name', 'title', 'features', 'price', 'module']
        
class ScholarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scholarship    
        fields = '__all__'
            