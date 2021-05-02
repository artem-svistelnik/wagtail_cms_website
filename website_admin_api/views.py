from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import json
class FeedbackView(APIView):
    def post(self,request):
        try:
            if type(request.data) is str:
                data = json.dumps(request.data)
            elif type(request.data) is dict:
                data = request.data
            else:
                data = json.loads(str(request.data))
            return Response({'Success': 'feedback data save'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({'Fail': 'data invalid'}, status=status.HTTP_400_BAD_REQUEST)
