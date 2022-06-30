from django.urls import path
from .views import SellerListView, SellerView, TopSellerView

urlpatterns = [
    path('', SellerListView.as_view()),
    path('topseller', TopSellerView.as_view()),
    path('<pk>', SellerView.as_view()),
]