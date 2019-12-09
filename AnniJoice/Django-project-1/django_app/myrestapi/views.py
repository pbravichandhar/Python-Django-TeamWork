from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, response
from .serializers import ToolSerializer
from .models import Tool
from bson.objectid import ObjectId


# Create your views here.

class HelloWorld(APIView):
    def get(self, request):
       serializer = ToolSerializer(Tool.objects.all(), many = True)
    #    serializer = ToolSerializer(Tool.objects(name= "anni",id=ObjectId(request.data.get("id"))), many = True)
       response = {"tools": serializer.data}
       return Response(response, status=status.HTTP_200_OK) 

class Mypostcall(APIView):
    def post(self, request):
        incomingdata = request.data
        
        callSerializer = ToolSerializer(data =incomingdata)
        if callSerializer.is_valid():

            tool = Tool(**incomingdata)
            tool.save()
            response = callSerializer.data
        return Response(incomingdata, status=status.HTTP_200_OK)

class Myputcall(APIView):
    
    def put(self, request, myId):
        putcalldata = request.data
        callSerializerputCall = ToolSerializer(data = putcalldata)
        if callSerializerputCall.is_valid():
            updatedata = Tool.objects(id=ObjectId(myId)).update(
                name = callSerializerputCall.data.get('name'),
                votes = callSerializerputCall.data.get('votes')
            )
            response = callSerializerputCall.data
        return Response(response, status=status.HTTP_200_OK)
    
class Mydeletecall(APIView):

    def delete(self, request, myId):
        Tool.objects(id=ObjectId(myId)).delete()
        return Response("Deleted Successfully", status=status.HTTP_200_OK)


