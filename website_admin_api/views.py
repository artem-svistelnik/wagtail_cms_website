from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import json
# from .models import Subscribers

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



#
# class GetSubscriptionView(APIView):
#     def post(self,request):
#         try:
#             if type(request.data) is str:
#                 data = json.dumps(request.data)
#             elif type(request.data) is dict:
#                 data = request.data
#             else:
#                 data = json.loads(str(request.data))
#
#             try:
#                 Subscribers.objects.get(email=data["email"])
#                 return Response({'Fail': 'This email has already exist'}, status=status.HTTP_400_BAD_REQUEST)
#             except Subscribers.DoesNotExist:
#                 new_subscriber=Subscribers.objects.create(email=data["email"])
#                 new_subscriber.save()
#                 return Response({'Success': 'New subscriber saved'}, status=status.HTTP_201_CREATED)
#         except Exception as e:
#             return Response({'Fail': 'data invalid',
#                              'Excaption':e}, status=status.HTTP_400_BAD_REQUEST)
