# from django.core.management.base import BaseCommand, CommandError, 
# from listings.models import Listing as Listing
# from datetime import datetime, timezone, timedelta

# class Command(BaseCommand):
#     help = 'Closes the specified listing for voting'

#     def handle(self):

#             Listing.objects.filter(date_expiry__lt=datetime.datetime.now()).delete()

#             self.stdout.write(self.style.SUCCESS('Successfully closed listing "%s"' % listing_id))