from courses.models import Course
from .models import Infostrip
from rest_framework import serializers


class CourseSerializers(serializers.ModelSerializer):

	class Meta:
		model = Course
		fields = '__all__'

class InfostripSerializers(serializers.ModelSerializer):

	class Meta:
		model = Infostrip
		fields = ('title', 'subtitle')