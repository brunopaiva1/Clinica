# views.py

from rest_framework import generics
from user.models import Item
from user.api.serializers import ItemSerializer

class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
