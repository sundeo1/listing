from django.urls import path
from .views import ListingsView, ListingView, SearchView, LivestockView, FashionView, FoodView, OthersView, EstateView

urlpatterns = [
    path('', ListingsView.as_view()),
    path('livestock', LivestockView.as_view()),
    path('fashion', FashionView.as_view()),
    path('food', FoodView.as_view()),
    path('real-estate', EstateView.as_view()),
    path('others', OthersView.as_view()),
    path('search', SearchView.as_view()),
    path('<slug>', ListingView.as_view()),
]