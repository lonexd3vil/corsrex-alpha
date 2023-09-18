from rest_framework import serializers
from home.models import *
from Profile.models import CustomUser

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
         model = CustomUser
         fields = ['username','is_verified']

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructer
        fields = ['id','instructer_name','instructer_profile','instructer_about']

class CourseIncludes(serializers.ModelSerializer):
    class Meta:
        model = CourseIncludes
        fields = ['id','title','icon']

class ShowcaseCourses(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id','updated_at','course_banner','course_title','rating','pricing']

class HomePageSerializer(serializers.ModelSerializer):
    showcase = ShowcaseCourses(many=True)
    class Meta:
        model = HomeModel
        fields = ['company_banner','company_logo','home_head','home_about','showcase']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = ['id','name']

class SingleCourseSeriealizer(serializers.ModelSerializer):
    teacher = InstructorSerializer(many=True)
    included = CourseIncludes(many=True)
    category = CategorySerializer()
    class Meta:
        model = Courses
        fields = ['id','updated_at','course_banner','course_title','rating','course_taglines','course_overview','category','benifits','pricing','base_currency','teacher','included',]

class BlogsSerializer(serializers.ModelSerializer):
    truncated_description = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ['id', 'updated_at', 'title', 'banner', 'truncated_description']

    def get_truncated_description(self, obj):
        return str(obj.description[:299] + "...")

class SingleBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'updated_at', 'title', 'banner', 'description']
