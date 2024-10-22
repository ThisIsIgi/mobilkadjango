from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from api.models import Student
from api.serializer import GradeSerializer

# Create your views here.

class StudentGradesView(APIView):
    def get(self, request, student_id):
        try:
            student = Student.objects.get(pk=student_id)
            grades = student.grades.all()
            grades_data =[GradeSerializer(g).data for g in grades]

            return JsonResponse(grades_data, safe=False)

        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)