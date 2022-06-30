from django.urls import path
from .views import ListingsView, ListingView

urlpatterns = [
    path('', ListingsView.as_view()),
    path('<slug>', ListingView.as_view()),
]