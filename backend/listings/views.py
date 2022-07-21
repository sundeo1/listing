from unicodedata import category
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Listing
from .serializers import ListingSerializer, listingDetailSerializer
from datetime import datetime, timezone, timedelta
from django.utils.timezone import now

class ListingsView(ListAPIView):
    queryset = Listing.objects.order_by('-list_date').filter(is_published=True, date_expired__gt=now())
    permission_classes = (permissions.AllowAny, )
    serializer_class = ListingSerializer
    lookup_field = 'slug'

class LivestockView(ListAPIView):
    queryset = Listing.objects.order_by('-list_date').filter(is_published=True, date_expired__gt=now(), category__name__iexact='Livestock')
    permission_classes = (permissions.AllowAny, )
    serializer_class = ListingSerializer
    lookup_field = 'slug'

class OthersView(ListAPIView):
    queryset = Listing.objects.order_by('-list_date').filter(is_published=True, date_expired__gt=now(), category__name__iexact='Others')
    permission_classes = (permissions.AllowAny, )
    serializer_class = ListingSerializer
    lookup_field = 'slug'

class FoodView(ListAPIView):
    queryset = Listing.objects.order_by('-list_date').filter(is_published=True, date_expired__gt=now(), category__name__iexact='Food')
    permission_classes = (permissions.AllowAny, )
    serializer_class = ListingSerializer
    lookup_field = 'slug'

class EstateView(ListAPIView):
    queryset = Listing.objects.order_by('-list_date').filter(is_published=True, date_expired__gt=now(), category__name__iexact='Real Estate')
    permission_classes = (permissions.AllowAny, )
    serializer_class = ListingSerializer
    lookup_field = 'slug'

class FashionView(ListAPIView):
    queryset = Listing.objects.order_by('-list_date').filter(is_published=True, date_expired__gt=now(), category__name__iexact='Fashion')
    permission_classes = (permissions.AllowAny, )
    serializer_class = ListingSerializer
    lookup_field = 'slug'

class ListingView(RetrieveAPIView):
    queryset = Listing.objects.order_by('-list_date').filter(is_published=True)
    permission_classes = (permissions.AllowAny, )
    serializer_class = listingDetailSerializer
    lookup_field = 'slug'

class SearchView(APIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = ListingSerializer

    def post(self, request, format=None):
        queryset = Listing.objects.order_by('-list_date').filter(is_published=True)
        data = self.request.data

        category = data['category']
        queryset = queryset.filter(category__name__iexact=category)

        price = data['price']
        if price == '0+':
            price = 0
        elif price == '200,000+':
            price = 200000
        elif price == '400,000+':
            price = 400000
        elif price == '600,000+':
            price = 600000
        elif price == '800,000+':
            price = 800000
        elif price == '1,000,000+':
            price = 1000000
        elif price == '1,200,000+':
            price = 1200000
        elif price == '1,500,000+':
            price = 1500000
        elif price == 'Any':
            price = -1
        
        if price != -1:
            queryset = queryset.filter(price__gte=price)
        
        days_passed = data['days_listed']
        if days_passed == '1 or less':
            days_passed = 1
        elif days_passed == '2 or less':
            days_passed = 2
        elif days_passed == '5 or less':
            days_passed = 5
        elif days_passed == '10 or less':
            days_passed = 10
        elif days_passed == '20 or less':
            days_passed = 20
        elif days_passed == 'Any':
            days_passed = 0
        
        for query in queryset:
            num_days = (datetime.now(timezone.utc) - query.list_date).days

            if days_passed != 0:
                if int(num_days) > int(days_passed):
                    slug=query.slug
                    queryset = queryset.exclude(slug__iexact=slug) 

        keywords = data['keywords']
        queryset = queryset.filter(description__icontains=keywords)

        serializer = ListingSerializer(queryset, many=True)

        return Response(serializer.data)

