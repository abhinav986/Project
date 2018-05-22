# from django.shortcuts import get_object_or_404, render, redirect
# from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from courses.models import Course
from .models import Infostrip, FooterStrip
from .serializers import InfostripSerializers
from courses.models import Category, Subcategory
from django.http import HttpResponse
import json


class HomeData(APIView):
	def getCourses(self, request, id):
		courses_development = []
		for subs in Subcategory.objects.all().filter(course_category_id=id):
			for course in Course.objects.all().filter(course_subcategory_id=subs.id):
				trainers = course.instructor_id.all()
				instructors = []
				for trainer in trainers:
					instructors.append(trainer.user_id.first_name +' '+ trainer.user_id.last_name)
				courses_development.append({
					'course_id' : course.id,
					'title' : course.title,
					'trainers' : instructors,
					'stars' : course.ratings,
					'price' : course.price,
					'discounted_price' : course.discount,
					'preview_image_url' : course.preview_image_url,
					'modal_data' : {
						'no_lectures' : course.no_lectures,
						'hours' : course.no_hours,
						'level' : course.level,
						'description' : course.description,
						'desc_points' : course.what_will_i_learn,
					}
				})
		return courses_development

	def get(self, request):
		try:
			courses_development = self.getCourses(request, 1)
			courses_design = self.getCourses(request, 3)
			courses_business = self.getCourses(request, 2)

			infostrips = Infostrip.objects.all()
			infostrips = InfostripSerializers(infostrips, many=True)

			footerstrips = FooterStrip.objects.all()
			f_strips = []
			for footerstrip in footerstrips:
				f_strips.append({
					'title' : footerstrip.title,
					'description' : footerstrip.description,
					'url' : footerstrip.url,
				})
		except Exception as e:
			return HttpResponse(json.dumps({'status':0,'error':str(e)}))

		return Response({
			'status':1,
			'homepagedata': {
				'infostrip' : infostrips.data,
				'courses' : [ 
					{ 'development' : courses_development },
					{ 'business' : courses_business },
					{ 'design' : courses_design },
				],
				'be_instructor' : f_strips[0],
				'for_business' : f_strips[1],
			}
		})