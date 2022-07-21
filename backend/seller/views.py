from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Seller
from .serializers import SellerSerializer
from datetime import datetime, timezone, timedelta
class SellerListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Seller.objects.filter(date_expired__lt=datetime.now())
    serializer_class = SellerSerializer
    pagination_class = None

class SellerView(RetrieveAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Seller.objects.filter(date_expired__lt=datetime.now())
    serializer_class = SellerSerializer

class TopSellerView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Seller.objects.filter(top_seller=True)
    serializer_class = SellerSerializer
    pagination_class = None