from django.contrib import admin
from ProdExChange.models import UserProfile,Item,OrderItem,Address,Payment

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Address)
admin.site.register(Payment)

