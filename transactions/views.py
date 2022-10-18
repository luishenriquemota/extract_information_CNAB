
from rest_framework.views import APIView, Request, Response, status
from rest_framework import generics
from transactions.models import Files
from transactions.serializers import UploadSerializer, ConvertFileSerializer
from utils.cnab_handler import read_cnab
from django.shortcuts import get_object_or_404
from types_transactions.models import Types
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
import ipdb

class UploadView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    queryset = Files.objects.all()
    serializer_class = UploadSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

   

class ConvertFileView(APIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]

    def post(self, request, id_file):
       
        file = get_object_or_404(Files, id=id_file)
        
        request_file = read_cnab(file.file)

        arr = []
        for item in request_file:
            retire_type = item.pop("type")

            select_type = get_object_or_404(Types, type=retire_type)
            
            serializer = ConvertFileSerializer(data=item)
            serializer.is_valid(raise_exception=True)
            serializer.save(type=select_type)
            arr.append(serializer.data)
        
   
        # ipdb.set_trace()
        # Files.delete(file)
        # os.remove(file.file.name)
    
        return Response(arr, status=status.HTTP_201_CREATED)
   
