from rest_framework import generics
from types_transactions.models import Types
from  types_transactions.serializers import TypeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication



class TypesView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]

    queryset = Types.objects.all()
    serializer_class = TypeSerializer
