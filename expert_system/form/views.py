from django.shortcuts import render
from rest_framework.views import APIView
from .models import ResponseModel
from .serializer import ResponseSerializer
from rest_framework.response import Response
from .mail import MailToCounseller

class ResponseView(APIView):
    def get(self,response):
        output = [{'name':output.name,
                   'registration':output.registration,
                   'email':output.email,
                   'desig':output.desig,
                   'department':output.department,
                   'year':output.year,
                   'type':output.type,
                   'grevience':output.grevience}
                   for output in ResponseModel.objects.all()]
        return Response(output)
    
    def post(self,response):
        serializer = ResponseSerializer(data = response.data)
        if serializer.is_valid(raise_exception=True):
            MailToCounseller(response.data)
            serializer.save()
            return Response(serializer.data)

# Create your views here.
