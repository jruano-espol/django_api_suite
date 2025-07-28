from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from firebase_admin import db
from datetime import datetime

class LandingAPI(APIView):
    name = "Landing API"
    collection_name = "votes"
    
    def get(self, request):
      ref = db.reference(f'{self.collection_name}')
      data = ref.get()
      return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        ref = db.reference(f'{self.collection_name}')

        current_time  = datetime.now()
        custom_format = current_time.strftime("%d/%m/%Y, %I:%M:%S %p").lower().replace('am', 'a. m.').replace('pm', 'p. m.')
        request.data.update({"timestamp": custom_format })

        new_resource = ref.push(request.data)
        return Response({"id": new_resource.key}, status=status.HTTP_201_CREATED)
