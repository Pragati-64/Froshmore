from django.contrib import admin
from .models import hostel, laundry, library, orders, tiffinservice, user_query

# Register your models here.
admin.site.register(user_query)
admin.site.register(hostel)
admin.site.register(tiffinservice)
admin.site.register(laundry)
admin.site.register(library)
admin.site.register(orders)