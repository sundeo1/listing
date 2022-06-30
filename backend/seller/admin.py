from django.contrib import admin
from .models import Seller

class SellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'date_onboarded')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    list_per_page = 25

admin.site.register(Seller, SellerAdmin)
